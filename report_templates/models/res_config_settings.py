from odoo import models, api


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @api.multi
    def edit_external_header(self):
        try:
            return super(ResConfigSettings, self).edit_external_header()
        except ValueError:
            return self._prepare_report_view_action('report_templates.external_layout_' + self.external_report_layout)

