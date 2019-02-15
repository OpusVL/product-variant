# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# © 2016 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# © 2019 OpusVL Peter Alabaster <peter.alabaster@opusvl.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def _update_taxes_id(self, vals):
        values = {'taxes_id': vals['taxes_id']}
        self.product_variant_ids.write(values)

    def _update_supplier_taxes_id(self, vals):
        values = {'supplier_taxes_id': vals['supplier_taxes_id']}
        self.product_variant_ids.write(values)

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'taxes_id' in vals:
            for product in self:
                product._update_taxes_id(vals)
        if 'supplier_taxes_id' in vals:
            for product in self:
                product._update_supplier_taxes_id(vals)
        return res

    @api.model
    def create(self, vals):
        product_tmpl = super(ProductTemplate, self).create(vals)
        if 'taxes_id' in vals:
            for product in product_tmpl:
                product._update_taxes_id(vals)
        if 'supplier_taxes_id' in vals:
            for product in self:
                product._update_supplier_taxes_id(vals)
        return product_tmpl
