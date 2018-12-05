# Copyright 2017 Jose Luis Sandoval Alaguna <jose.alaguna@rotafilo.com.tr>
from odoo import models


class MrpBomLine(models.Model):
    _inherit = ['mrp.bom.line', 'product.configurator']
    _name = 'mrp.bom.line'
