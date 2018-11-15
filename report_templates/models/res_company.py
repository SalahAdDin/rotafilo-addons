from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    external_report_layout = fields.Selection([
        ('background', 'Background'),
        ('boxed', 'Boxed'),
        ('clean', 'Clean'),
        ('custom', 'Custom'),
        ('standard', 'Standard'),
    ], string='Document Template')
