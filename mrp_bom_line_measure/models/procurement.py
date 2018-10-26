from odoo import models
from odoo import fields
from odoo import api
from odoo import _

from odoo.exceptions import UserError


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    def _get_stock_move_values(self, product_id, measure, measure_uom_id, product_qty, product_uom, location_id, name, origin, values, group_id):
        data =super(ProcurementGroup, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, values, group_id)
        data['measure']=measure
        data['measure_uom_id']=measure_uom_id
        return data
