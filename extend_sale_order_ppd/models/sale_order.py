from odoo import models, fields, exceptions
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Define the customer_po field
    customer_po = fields.Char(string='Customer PO', store=True)
    subject = fields.Char(string='Subject')
    def action_confirm(self):
        # Check if customer_po is empty
        if not self.customer_po:
            raise UserError("Customer PO Number is required and cannot be empty.")

        # Call the original action_confirm method from sale.order
        return super(SaleOrder, self).action_confirm()

