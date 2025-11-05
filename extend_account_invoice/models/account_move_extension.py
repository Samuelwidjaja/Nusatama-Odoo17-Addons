# extend_account_invoice/models/account_move_extension.py
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sbu_jurnal = fields.Selection(
        [('Pusat', 'Pusat'), ('KSO', 'KSO')],
        string='SBU Jurnal',
    )

    # Tambahkan field Customer PO
    customer_po = fields.Char(
        string='Customer PO',
        store=True,
        readonly=False
    )

    @api.model
    def create(self, vals):
        move = super(AccountMove, self).create(vals)
        if move.invoice_origin:
            sale_order = self.env['sale.order'].search(
                [('name', '=', move.invoice_origin)], limit=1
            )
            if sale_order:
                move.customer_po = sale_order.customer_po
        return move
