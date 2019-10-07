# -*- coding: utf-8 -*-

##############################################################################
# Product Weight with Scale
# Copyright (C) 2018 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, api, fields


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

    @api.onchange('uom_id')
    def _onchange_uom_id(self):
        if self.uom_id:
            self.uom_category_name = self.uom_id.category_id.name
