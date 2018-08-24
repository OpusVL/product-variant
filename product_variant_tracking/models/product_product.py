# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    tracking = fields.Selection([
        ('serial', 'By Unique Serial Number'),
        ('lot', 'By Lots'),
        ('none', 'No Tracking')], string="Tracking", default='none', required=True)

    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        template_vals = {}
        if 'tracking' not in vals:
            template_vals[
                'tracking'] = product.product_tmpl_id.tracking
        if template_vals:
            product.write(template_vals)
        return product
