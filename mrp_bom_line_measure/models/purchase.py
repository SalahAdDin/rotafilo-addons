"""
Created on 19/09/2018
@author: salahaddin
"""

from odoo import models
from odoo import fields
from odoo import api
from odoo import _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    measure = fields.Char(_('Measure'))
    measure_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        help="Unit of Measure (Unit of Measure) is the unit of measurement for the products measure"
    )


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _prepare_purchase_order_line(self, product_id, measure, measure_uom_id, product_qty, product_uom, values, po,
                                     supplier):
        result = super(PurchaseOrderLine, self)._prepare_purchase_order_line(product_id, product_qty, product_uom,
                                                                             values, po, supplier)
        result['measure'] = measure
        result['measure_uom_id'] = measure_uom_id

        return result
