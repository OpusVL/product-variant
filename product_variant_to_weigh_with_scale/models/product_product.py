# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusLV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    to_weight = fields.Boolean(
        string='To Weigh With Scale',
        help="Check if the product should be weighted using the hardware scale integration"
    )

    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        template_vals = {}
        if 'to_weight' not in vals:
            template_vals[
                'to_weight'] = product.product_tmpl_id.to_weight
        if template_vals:
            product.write(template_vals)
        return product
