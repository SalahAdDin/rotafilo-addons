"""
Created on 19/09/2018
@author: salahaddin
"""

from odoo import models
from odoo import fields
from odoo import api
from odoo import _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.multi
    def button_inform(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']

        try:
            template_id = ir_model_data.get_object_reference('mail_inform_purchase', 'email_template_inform_purchase')[
                1]
        except ValueError:
            template_id = False

        template_obj = self.env['mail.template'].search([('id', '=', template_id)])
        boss = self.env['res.partner'].search([('function', '=', 'CEO')])

        body_raw = template_obj.body_html. \
            replace('${record_name}', self.name) \
            .replace('${current.url}', '{}'.format(self.env['ir.config_parameter'].get_param('web.base.url'))) \
            .replace('${company.id}', '{}'.format(self.env.user.company_id.id)) \
            .replace('${company.name}', self.env.user.company_id.name) \
            .replace('${company.phone}', '{}'.format(self.env.user.company_id.phone or '')) \
            .replace(
            '${company.email}',
            '<a href="mailto:{0}" style="text-decoration:none; color: white;">{0}</a><br/>'.format(
                self.env.user.company_id.email
            ) if self.env.user.company_id.email else '') \
            .replace(
            '${company.website}',
            '<a href="{0}" style="text-decoration:none; color: white;">{0}</a>'.format(
                self.env.user.company_id.website
            ) if self.env.user.company_id.website else '') \
            .replace('${user_id.signature}',
                     self.env.user.signature if self.env.user and self.env.user.signature else '') \
            .replace('${boss.name}', boss.name)

        for line in self.order_line:

            procurement_group = line.procurement_group_id
            product = self.env['sale.order'].search([('id', '=', procurement_group.sale_id.id)]).order_line[0].name
            sub_total = line.price_subtotal
            purchase_order_lines_list = self.env['purchase.order.line'].search(
                [('procurement_group_id', '=', procurement_group.id)]
            )
            total = 0
            for line in purchase_order_lines_list:
                if line.order_id.state != 'cancel':
                    total += line.price_subtotal

            body = body_raw.replace('${procurement_group.name}', procurement_group.name) \
                .replace('${product}', product) \
                .replace('${sub_total}', str(sub_total)) \
                .replace('${currency_id.symbol}', '{}'.format(line.currency_id.symbol)) \
                .replace('${total}', str(total))
            values = {
                'model': 'purchase.order',
                'res_id': self.id,
                'subject': "{0} for {1}".format(self.name, procurement_group.name),
                'email_to': boss.email,
                # 'partner_ids': [boss.id],
                'email_from': self.env.user.email,
                'lang': boss.lang,
                'body_html': body,
            }

            self.env['mail.mail'].create(values).send()

        return True
