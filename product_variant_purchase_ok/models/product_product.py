# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    purchase_ok = fields.Boolean('Can be Purchased', default=True)

    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        template_vals = {}
        if 'purchase_ok' not in vals:
            template_vals[
                'purchase_ok'] = product.product_tmpl_id.purchase_ok
        if template_vals:
            product.write(template_vals)
        return product
