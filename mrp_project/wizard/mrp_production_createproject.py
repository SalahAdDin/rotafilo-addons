from odoo import api, fields, models, _
from odoo.exceptions import UserError


class MrpProductionCreateProject(models.TransientModel):
    """ wizard to create a Project from a Manufacturing Order """
    _name = "mrp.production.createproject"

    mrp_production_id = fields.Many2one('mrp.production', string='Production', domain=[('type', '=', 'production')])
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        help=_("Leave it blank if you want create a new project with the manufacturing order's name as default name.")
    )

    @api.multi
    def action_create_project_task(self):
        self.ensure_one()
        # get the production to update
        production = self.mrp_production_id
        project = self.project_id

        # If this production come from a sale order and that order
        # has an analytic account assigned, then project is child of
        # that analytic account

        obj_production = self.env['mrp.production']
        obj_order = self.env['sale.order']

        # if related `project_id` is empty
        if not project.id and not production.project_id:
            # if `sale_id` field exist in production's fields and `related_project_id` field exist in sale order's fields
            if 'sale_id' in obj_production._fields and 'related_project_id' in obj_order._fields:
                # getting the sale order source
                sale_order = production.sale_id
                if sale_order :
                    # getting the sale order's related project
                    project = sale_order.related_project_id
                    if project.id:
                        production.write({
                            'analytic_account_id': project.analytic_account_id.id
                        })
                    else:
                        # create new project.project
                        production.action_create_project()
                else:
                    # create new project.project
                    production.action_create_project()
            else:
                # create new project.project
                production.action_create_project()
        # if project but production is not related to that project
        elif project.id and not production.project_id:
            # update mrp.production.project_id with the selected project.project.id
            production.write({
                'analytic_account_id': project.analytic_account_id.id
            })
        # else
        else:
            raise UserError(_(
                'This manufacturing order already has a related project. Order: {0}, Project: {1}'.format(
                    production,
                    production.project_id
                )
            ))

        return True
