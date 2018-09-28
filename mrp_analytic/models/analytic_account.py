# © 2015 Pedro M. Baeza - Antiun Ingeniería
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models, fields


class AnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    def _compute_num_productions(self):
        for analytic_account in self:
            analytic_account.num_productions = self.env['mrp.production'].search_count([
                ('analytic_account_id', '=', analytic_account.id)
            ])

    num_productions = fields.Integer(compute="_compute_num_productions")
