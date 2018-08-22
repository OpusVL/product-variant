# -*- coding: utf-8 -*-
# Copyright 2018 Peter Alabaster - OpusVL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def post_init_hook(cr, registry):
    """
    This post-init-hook will update all existing product.product
    available_in_pos
    """
    cr.execute(
        """
        UPDATE product_product
        SET uom_id = product_template.uom_id,
            uom_po_id = product_template.uom_po_id
        FROM product_template
        WHERE product_template.id = product_product.product_tmpl_id
        """)
