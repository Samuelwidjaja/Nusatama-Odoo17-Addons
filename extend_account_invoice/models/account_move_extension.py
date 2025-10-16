# extend_account_invoice/models/account_move_extension.py
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    sbu_jurnal = fields.Selection(
        [('Pusat', 'Pusat'), ('KSO', 'KSO')],
        string='SBU Jurnal',
    )
