from odoo import models, fields, api
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    quotation_attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Quotation Attachments',
        help="Attach up to 2 quotation PDF files related to this Purchase Order.",
    )

    @api.model
    def create(self, vals):
        """Perbaikan bug Odoo:
        Saat file diupload sebelum record disimpan, ir.attachment akan punya res_id=0.
        Akibatnya, user lain tidak bisa melihat file itu setelah PO dibuat.
        Maka kita tautkan ulang attachment ke record PO setelah create().
        """
        records = super(PurchaseOrder, self).create(vals)
        for rec in records:
            if rec.quotation_attachment_ids:
                rec.quotation_attachment_ids.write({
                    'res_model': self._name,
                    'res_id': rec.id
                })
        return records

    def button_confirm(self):
        """Validasi jumlah file quotation sebelum konfirmasi PO"""
        for order in self:
            attachments = order.quotation_attachment_ids
            if not attachments:
                raise UserError("Please attach at least one quotation file before confirming the Purchase Order.")
            if len(attachments) > 2:
                raise UserError("You can attach a maximum of 2 quotation files.")
        return super(PurchaseOrder, self).button_confirm()
