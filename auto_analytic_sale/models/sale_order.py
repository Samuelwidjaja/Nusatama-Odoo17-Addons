from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
from odoo import SUPERUSER_ID

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()

        if not self.analytic_account_id:
            self._saleorder_analytic_account_value()

        return result

    def _saleorder_analytic_account_value(self):
        result = {}
        # Cari analytic plan default
        default_plan = self.env['account.analytic.plan'].search([], limit=1)
        if not default_plan:
            raise UserError(_("No Analytic Plan found. Please create one in Accounting > Configuration > Analytic Plans."))

        new_analytic = self.env["account.analytic.account"].with_user(SUPERUSER_ID).create({
            "name": self.name,
            "partner_id": self.partner_id.id,
            "plan_id": default_plan.id, 
        })
        self.write({"analytic_account_id": new_analytic.id})
        result[self.id] = new_analytic
        return result
