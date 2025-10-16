from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    sbu = fields.Selection([
        ('utama', 'Utama'),
        ('kso', 'KSO'),
    ], string="SBU")
