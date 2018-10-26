from odoo import models, fields, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    measure = fields.Char(_('Measure'))
    measure_uom_id = fields.Many2one(
        'product.uom',
        _('Unit of Measure'),
        help="Unit of Measure (Unit of Measure) is the unit of measurement for the products measure")
