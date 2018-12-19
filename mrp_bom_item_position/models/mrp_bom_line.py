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
        size=4
    )
