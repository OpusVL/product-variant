# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class ProductVariantSaleOk(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(ProductVariantToWeight, self).setUp(
            *args, **kwargs)
        # template
        self.template_model = self.env['product.template']
        self.product_template = self.template_model.create({
            'name': 'Product Template',
            'sale_ok': True,
        })
        # variants
        self.product_model = self.env['product.product']
        self.product_1 = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
        })
        self.product_2 = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
        })
        return result

    def test_post_init_hook(self):
        from ..hooks import post_init_hook
        self.product_template.product_variant_ids.write({
            'sale_ok': False,
        })
        post_init_hook(self.cr, None)
        self.product_template.product_variant_ids.invalidate_cache()
        self.assertEqual(
            self.product_template.sale_ok,
            self.product_1.sale_ok)
        self.assertEqual(
            self.product_template.sale_ok,
            self.product_2.sale_ok)

    def test_create_product_template(self):
        new_template = self.template_model.create({
            'name': 'New Product Template',
            'sale_ok': True,
        })
        self.assertEqual(
            new_template.sale_ok,
            new_template.product_variant_ids.sale_ok)

    def test_create_variant(self):
        new_variant = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
        })
        self.assertEqual(
            self.product_template.sale_ok,
            new_variant.sale_ok)

    def test_update_variant(self):
        self.product_1.sale_ok = False
        self.assertNotEqual(
            self.product_1.sale_ok,
            self.product_1.product_tmpl_id.sale_ok)

    def test_update_template_variant(self):
        self.product_1.product_tmpl_id.sale_ok = False
        for variant in self.product_1.product_tmpl_id.product_variant_ids:
            self.assertEqual(
                self.product_1.sale_ok, variant.sale_ok)
