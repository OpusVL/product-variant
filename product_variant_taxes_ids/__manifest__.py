# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# © 2019 OpusVL Peter Alabaster <peter.alabaster@opusvl.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product taxes ids per variant',
    'summary': 'Taxes ids to product variant scope',
    'version': '10.0.1.0.0',
    'author': 'OpusVL'
              'Odoo Community Association (OCA)',
    'category': 'Product Management',
    'depends': [
        'product',
        'account',
    ],
    'data': [
        'views/product_product_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'post_init_hook': 'post_init_hook',
}
