# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    # Need to also redeclare the default function that's on product.template
    def _get_default_uom_id(self):
        return self.env["product.uom"].search([], limit=1, order='id').id

    uom_id = fields.Many2one(
        'product.uom', 'Unit of Measure',
        default=_get_default_uom_id, required=True,
        help="Default Unit of Measure used for all stock operation.")
    uom_po_id = fields.Many2one(
        'product.uom', 'Purchase Unit of Measure',
        default=_get_default_uom_id, required=True,
        help="Default Unit of Measure used for purchase orders. It must be in the same category than the default unit of measure.")

    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        template_vals = {}
        if 'uom_id' not in vals:
            template_vals[
                'uom_id'] = product.product_tmpl_id.uom_id.id
        if 'uom_po_id' not in vals:
            template_vals[
                'uom_po_id'] = product.product_tmpl_id.uom_po_id.id
        if template_vals:
            product.write(template_vals)
        return product
