# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def _update_purchase_ok(self, vals):
        values = {'purchase_ok': vals['purchase_ok']}
        self.product_variant_ids.write(values)

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'purchase_ok' in vals:
            for product in self:
                product._update_purchase_ok(vals)
        return res

    @api.model
    def create(self, vals):
        product_tmpl = super(ProductTemplate, self).create(vals)
        if 'purchase_ok' in vals:
            for product in product_tmpl:
                product._update_purchase_ok(vals)
        return product_tmpl
