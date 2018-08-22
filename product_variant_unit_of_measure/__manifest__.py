# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Variant Unit of Measure',
    'summary': 'Unit of Measure in product level',
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
    ],
    'post_init_hook': 'post_init_hook',
}
