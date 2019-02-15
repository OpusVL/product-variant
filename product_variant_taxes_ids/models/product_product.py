# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# © 2016 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# © 2019 OpusVL Peter Alabaster <peter.alabaster@opusvl.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    taxes_id = fields.Many2many(
        'account.tax',
        'product_taxes_rel_variant',
        'prod_id',
        'tax_id',
        string='Customer Taxes',
        domain=[('type_tax_use', '=', 'sale')]
    )
    supplier_taxes_id = fields.Many2many(
        'account.tax',
        'product_supplier_taxes_rel_variant',
        'prod_id',
        'tax_id',
        string='Vendor Taxes',
        domain=[('type_tax_use', '=', 'purchase')]
    )

    @api.model
    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        template_vals = {}
        if 'taxes_id' not in vals:
            template_vals['taxes_id'] = product.product_tmpl_id.taxes_id
        if 'supplier_taxes_id' not in vals:
            template_vals['supplier_taxes_id'] = product.product_tmpl_id.supplier_taxes_id
        if template_vals:
            product.write(template_vals)
        return product
