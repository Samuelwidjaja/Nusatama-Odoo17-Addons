from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Related field agar otomatis mengikuti dari Sales Order
    customer_po = fields.Char(
        related='sale_id.customer_po',
        string="Customer PO",
        store=True,
        readonly=True,
    )
