# extend_stock_picking_po/models/stock_picking.py
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_po = fields.Char(
        string="Customer PO",
        compute="_compute_customer_po",
        store=True,
        readonly=True,
    )

    @api.depends(
        'group_id', 
        'group_id.sale_id.customer_po',
        'move_ids_without_package.sale_line_id.order_id.customer_po'
    )
    def _compute_customer_po(self):
        for picking in self:
            # Prioritas: procurement group -> sale_id
            sale = picking.group_id.sale_id
            if not sale:
                # Fallback: ambil dari move lines (jaga-jaga jika group kosong)
                sale = (picking.move_ids_without_package
                        .mapped('sale_line_id.order_id')[:1] or False)
                sale = sale[0] if sale else False
            picking.customer_po = sale.customer_po if sale else False
