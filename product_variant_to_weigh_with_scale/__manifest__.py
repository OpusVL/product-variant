# -*- coding: utf-8 -*-

##############################################################################
# Product Weight with Scale
# Copyright (C) 2019 OpusVL (<http://opusvl.com/>)
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

{
    'name': 'Product Variant To Weigh With Scale',
    'summary': 'To Weight With Scale in product level',
    'version': '11.0.1.0.0',
    'category': 'Point Of Sale',
    'license': 'AGPL-3',
    'author': 'OpusVL, Odoo Community Association (OCA)',
    'website': 'https://opusvl.com/',
    'data': [
        'views/product_view.xml',
    ],
    'depends': [
        'point_of_sale',
        'product_variant_available_in_pos',
    ],
    'post_init_hook': 'post_init_hook',
}
