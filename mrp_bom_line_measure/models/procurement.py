from odoo import models
from odoo import fields
from odoo import api
from odoo import _

from odoo.exceptions import UserError


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def run(self, product_id, measure, measure_uom_id, product_qty, product_uom, location_id, name, origin, values):
        values.setdefault('company_id', self.env['res.company']._company_default_get('procurement.group'))
        values.setdefault('priority', '1')
        values.setdefault('date_planned', fields.Datetime.now())
        rule = self._get_rule(product_id, location_id, values)

        if not rule:
            raise UserError(_('No procurement rule found. Please verify the configuration of your routes'))

        getattr(rule, '_run_%s' % rule.action)(product_id, measure, measure_uom_id, product_qty, product_uom,
                                               location_id, name, origin, values)
        return True
