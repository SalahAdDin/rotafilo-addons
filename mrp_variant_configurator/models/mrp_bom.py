# Copyright 2017 Jose Luis Sandoval Alaguna <jose.alaguna@rotafilo.com.tr>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    @api.multi
    def write(self):
        product_obj = self.env['product.product']
        lines = self.mapped('order_line').filtered(lambda x: not x.product_id)
        for line in lines:
            product = product_obj._product_find(
                line.product_tmpl_id, line.product_attribute_ids,
            )
            if not product:
                values = line.product_attribute_ids.mapped('value_id')
                product = product_obj.create({
                    'product_tmpl_id': line.product_tmpl_id.id,
                    'attribute_value_ids': [(6, 0, values.ids)],
                })
            line.write({'product_id': product.id})
        super(MrpBom, self).action_confirm()


class MrpBomLine(models.Model):
    _inherit = ['mrp.bom.line', 'product.configurator']
    _name = 'mrp.bom.line'
