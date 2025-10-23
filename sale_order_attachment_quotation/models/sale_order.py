from odoo import models, fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Many2many untuk simpan file PDF quotation
    quotation_attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Quotation Attachments',
        help="Attach up to 2 quotation PDF files."
    )

    def action_confirm(self):
        """Validasi jumlah file quotation sebelum konfirmasi"""
        for order in self:
            attachments = order.quotation_attachment_ids
            if not attachments:
                raise UserError("You must attach at least one quotation PDF before confirming the order.")
            if len(attachments) > 2:
                raise UserError("You can only attach a maximum of 2 quotation PDF files.")
        return super(SaleOrder, self).action_confirm()

    def action_open_quotation_attachments(self):
        """Buka jendela upload / lihat attachment quotation"""
        self.ensure_one()
        return {
            'name': 'Quotation Attachments',
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'view_mode': 'tree,form',
            'domain': [
                ('res_model', '=', 'sale.order'),
                ('res_id', '=', self.id),
                ('description', '=', 'quotation_attachment')
            ],
            'context': {
                'default_res_model': 'sale.order',
                'default_res_id': self.id,
                'default_description': 'quotation_attachment',
            },
            'target': 'current',
        }
