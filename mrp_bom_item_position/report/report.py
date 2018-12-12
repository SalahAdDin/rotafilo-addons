"""
Created on 19/09/2018
@author: salahaddin
"""

from odoo import models, api


class BomStructureReport(models.AbstractModel):
    _inherit = 'report.mrp.mrp_bom_structure_report'

    @api.model
    def _get_child_vals(self, record, level, qty, uom):
        child = super(BomStructureReport, self)._get_child_vals(record, level, qty, uom)
        child['p_item_num'] = record.item_num

        return child
