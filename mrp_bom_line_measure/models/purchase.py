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

    origin = fields.Char(
        'Source Document',
        copy=False,
        help="Reference of the document that generated this purchase order "
             "request (e.g. a sales order)"
    )


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _run_buy(self, product_id, product_qty, product_uom, location_id, name, origin,
                 values):
        cache = {}
        suppliers = product_id.seller_ids \
            .filtered(lambda r: (not r.company_id or r.company_id == values['company_id']) and (
                not r.product_id or r.product_id == product_id))
        if not suppliers:
            msg = _('There is no vendor associated to the product %s. Please define a vendor for this product.') % (
                product_id.display_name,)
            raise UserError(msg)

        supplier = self._make_po_select_supplier(values, suppliers)
        partner = supplier.name

        domain = self._make_po_get_domain(values, partner)

        if domain in cache:
            po = cache[domain]
        else:
            po = self.env['purchase.order'].sudo().search([dom for dom in domain])
            po = po[0] if po else False
            cache[domain] = po
        if not po:
            vals = self._prepare_purchase_order(product_id, product_qty, product_uom, origin, values, partner)
            company_id = values.get('company_id') and values['company_id'].id or self.env.user.company_id.id
            po = self.env['purchase.order'].with_context(force_company=company_id).sudo().create(vals)
            cache[domain] = po
        elif not po.origin or origin not in po.origin.split(', '):
            if po.origin:
                if origin:
                    po.write({'origin': po.origin + ', ' + origin})
                else:
                    po.write({'origin': po.origin})
            else:
                po.write({'origin': origin})

        # Create Line
        po_line = False
        for line in po.order_line:
            if line.product_id == product_id and line.product_uom == product_id.uom_po_id:
                if line._merge_in_existing_line(product_id, measure, measure_uom_id, product_qty, product_uom,
                                                location_id, name, origin,
                                                values):
                    vals = self._update_purchase_order_line(product_id, measure, measure_uom_id, product_qty,
                                                            product_uom, values, line, partner)
                    po_line = line.write(vals)
                    break
        if not po_line:
            vals = self._prepare_purchase_order_line(product_id, measure, measure_uom_id, product_qty, product_uom,
                                                     values, po, supplier)
            self.env['purchase.order.line'].sudo().create(vals)

    @api.multi
    def _prepare_purchase_order_line(self, product_id, measure, measure_uom_id, product_qty, product_uom, values, po,
                                     supplier):
        result = super(PurchaseOrderLine, self)._prepare_purchase_order_line(product_id, product_qty, product_uom,
                                                                             values, po, supplier)
        result['measure'] = measure
        result['measure_uom_id'] = measure_uom_id

        return result
