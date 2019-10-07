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

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    uom_category_name = fields.Char(string="UOM Category Name", compute='_compute_uom_category_name', store=True)

    def _update_to_weight(self, vals):
        values = {'to_weight': vals['to_weight']}
        self.product_variant_ids.write(values)

    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'to_weight' in vals:
            for product in self:
                product._update_to_weight(vals)
        return res

    @api.model
    def create(self, vals):
        product_tmpl = super(ProductTemplate, self).create(vals)
        if 'to_weight' in vals:
            for product in product_tmpl:
                product._update_to_weight(vals)
        return product_tmpl

    @api.multi
    @api.depends('uom_id')
    def _compute_uom_category_name(self):
        for record in self:
            record.uom_category_name = record.uom_id.category_id.name

    @api.onchange('uom_id')
    def _onchange_uom_id(self):
        res = super(ProductTemplate, self)._onchange_uom_id()
        if self.uom_id:
            self.uom_category_name = self.uom_id.category_id.name
        return res
