# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def _update_uom_id(self, vals):
        values = {'uom_id': vals['uom_id']}
        self.product_variant_ids.write(values)

    def _update_uom_po_id(self, vals):
        values = {'uom_po_id': vals['uom_po_id']}
        self.product_variant_ids.write(values)

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'uom_id' in vals:
            for product in self:
                product._update_uom_id(vals)
        if 'uom_po_id' in vals:
            for product in self:
                product._update_uom_po_id(vals)
        return res

    @api.model
    def create(self, vals):
        product_tmpl = super(ProductTemplate, self).create(vals)
        if 'uom_id' in vals:
            for product in product_tmpl:
                product._update_uom_id(vals)
        if 'uom_po_id' in vals:
            for product in product_tmpl:
                product._update_uom_po_id(vals)
        return product_tmpl
