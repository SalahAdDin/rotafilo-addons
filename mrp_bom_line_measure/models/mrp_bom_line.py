"""
Created on 19/09/2018
@author: salahaddin
"""

from odoo import models
from odoo import fields
from odoo import _


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    item_num = fields.Char(
        _('CAD Item Position'),
        help=_(
            "This is the item reference position into the CAD "
            "document that declares this BoM."
        ),
        size=3
    )
    measure = fields.Char(
        _('Measure'),
        help=_(
            "Type the measure without blank spaces and un lowercase: ##x##"
        )
    )
    measure_uom_id = fields.Many2one(
        'product.uom',
        'Unit of Measure',
        help=_("Unit of Measure (Unit of Measure) is the unit of measurement"
               "for the products measure")
    )
