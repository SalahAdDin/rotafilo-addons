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
