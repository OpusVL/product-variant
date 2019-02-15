# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# © 2019 OpusVL Peter Alabaster <peter.alabaster@opusvl.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.tests.common import TransactionCase


class ProductVariantTaxesIds(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(ProductVariantTaxesIds, self).setUp(
            *args, **kwargs)
        # template - set any sale / purchase taxes in the system
        self.tax_group_id = self.env['account.tax.group'].create(dict(
            name='Tax Group A',
        ))
        self.taxes_id = self.env['account.tax'].create(dict(
            name='Sales Tax A',
            type_tax_use='sale',
            amount_type='percent',
            amount=20,
            tax_group_id=self.tax_group_id.id,
        ))
        self.supplier_taxes_id = self.env['account.tax'].create(dict(
            name='Purchase Tax A',
            type_tax_use='purchase',
            amount_type='percent',
            amount=20,
            tax_group_id=self.tax_group_id.id,
        ))
        self.template_model = self.env['product.template']
        self.product_template = self.template_model.create({
            'name': 'Product Template',
            'taxes_id': self.taxes_id,
            'supplier_taxes_id': self.supplier_taxes_id,
        })
        # variants
        self.product_model = self.env['product.product']
        self.product_1 = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
            'name': 'Variant A',
        })
        self.product_2 = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
            'name': 'Variant B',
        })
        return result

    def test_post_init_hook(self):
        from ..hooks import post_init_hook
        self.product_template.product_variant_ids.write({
            'taxes_id': False,
            'supplier_taxes_id': False,
        })
        post_init_hook(self.cr, None)
        self.product_template.product_variant_ids.invalidate_cache()
        self.assertEqual(
            self.product_template.taxes_id,
            self.product_1.taxes_id,
            "Variant should have the same tax as its template after post_init_hook is run")
        self.assertEqual(
            self.product_template.taxes_id,
            self.product_2.taxes_id,
            "Variant should have the same tax as its template after post_init_hook is run")
        self.assertEqual(
            self.product_template.supplier_taxes_id,
            self.product_1.supplier_taxes_id,
            "Variant should have the same purchase tax as its template after post_init_hook is run")
        self.assertEqual(
            self.product_template.supplier_taxes_id,
            self.product_2.supplier_taxes_id,
            "Variant should have the same purchase tax as its template after post_init_hook is run")

    def test_create_product_template(self):
        new_template = self.template_model.create({
            'name': 'New Product Template',
            'taxes_id': False,
            'supplier_taxes_id': False,
        })
        self.assertEqual(
            new_template.taxes_id,
            new_template.product_variant_ids.taxes_id,
            "Newly created template should have the same tax as its variants")
        self.assertEqual(
            new_template.supplier_taxes_id,
            new_template.product_variant_ids.supplier_taxes_id,
            "Newly created template should have the same purchase tax as its variants")

    def test_create_variant(self):
        new_variant = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
        })
        self.assertEqual(
            self.product_template.taxes_id,
            new_variant.taxes_id,
            "Newly created variant should have the same tax as its template")
        self.assertEqual(
            self.product_template.supplier_taxes_id,
            new_variant.taxes_id,
            "Newly created variant should have the same purchase tax as its template")

    def test_update_variant(self):
        self.product_1.taxes_id = [[4, self.taxes_id.id]]
        self.product_1.supplier_taxes_id = [[4, self.supplier_taxes_id.id]]
        self.assertNotEqual(
            self.product_1.taxes_id,
            self.product_1.product_tmpl_id.taxes_id,
            "After writing a new tax to a variant, the tax should differ from the template tax")
        self.assertNotEqual(
            self.product_1.supplier_taxes_id,
            self.product_1.product_tmpl_id.supplier_taxes_id,
            "After writing a new purchase tax to a variant, the purchase tax should differ from the template purchase tax")

    def test_update_template_variant(self):
        self.product_1.product_tmpl_id.taxes_id = False
        self.product_1.product_tmpl_id.supplier_taxes_id = False
        for variant in self.product_1.product_tmpl_id.product_variant_ids:
            self.assertEqual(
                self.product_1.taxes_id, variant.taxes_id,
                "Tax should have propagated from template to all variants")
            self.assertEqual(
                self.product_1.supplier_taxes_id, variant.supplier_taxes_id,
                "Purchase tax should have propagated from template to all variants")
