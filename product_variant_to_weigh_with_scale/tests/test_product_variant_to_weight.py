# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class ProductVariantToWeight(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(ProductVariantToWeight, self).setUp(
            *args, **kwargs)
        # template
        self.template_model = self.env['product.template']
        self.product_template = self.template_model.create({
            'name': 'Product Template',
            'to_weight': True,
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
            'to_weight': False,
        })
        post_init_hook(self.cr, None)
        self.product_template.product_variant_ids.invalidate_cache()
        self.assertEqual(
            self.product_template.to_weight,
            self.product_1.to_weight)
        self.assertEqual(
            self.product_template.to_weight,
            self.product_2.to_weight)

    def test_create_product_template(self):
        new_template = self.template_model.create({
            'name': 'New Product Template',
            'to_weight': True,
        })
        self.assertEqual(
            new_template.to_weight,
            new_template.product_variant_ids.to_weight)

    def test_create_variant(self):
        new_variant = self.product_model.create({
            'product_tmpl_id': self.product_template.id,
        })
        self.assertEqual(
            self.product_template.to_weight,
            new_variant.to_weight)

    def test_update_variant(self):
        self.product_1.to_weight = False
        self.assertNotEqual(
            self.product_1.to_weight,
            self.product_1.product_tmpl_id.to_weight)

    def test_update_template_variant(self):
        self.product_1.product_tmpl_id.to_weight = False
        for variant in self.product_1.product_tmpl_id.product_variant_ids:
            self.assertEqual(
                self.product_1.to_weight, variant.to_weight)
