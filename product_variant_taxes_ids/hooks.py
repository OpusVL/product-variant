# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# © 2016 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# © 2019 OpusVL Peter Alabaster <peter.alabaster@opusvl.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
	"""
	This post-init-hook will copy across all existing product.product
	taxes_id and supplier_taxes_id
	"""
	env = api.Environment(cr, SUPERUSER_ID, {})
	for product in env['product.product'].search([]):
		for tax in product.product_tmpl_id.taxes_id:
			product.taxes_id = [[4, tax.id]]
		for supp_tax in product.product_tmpl_id.supplier_taxes_id:
			product.supplier_taxes_id = [[4, supp_tax.id]]
