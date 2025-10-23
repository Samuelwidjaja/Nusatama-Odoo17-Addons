from odoo import models, fields
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    quotation_attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Quotation Attachments',
        help="Attach up to 2 quotation PDF files related to this Purchase Order.",
    )

    def button_confirm(self):
        for order in self:
            if not order.quotation_attachment_ids:
                raise UserError("Please attach at least one quotation PDF before confirming the Purchase Order.")
            if len(order.quotation_attachment_ids) > 2:
                raise UserError("You can attach a maximum of 2 quotation PDF files.")
        return super(PurchaseOrder, self).button_confirm()
