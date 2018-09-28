from odoo import models, fields, api, _
from odoo.exceptions import UserError
from email.utils import formataddr


################
# Mail.Message #
################
class PRTMailMessage(models.Model):
    _name = "mail.message"
    _inherit = "mail.message"

    """
    Check settings and use company's email if forced.
    Make 'From:' look like 'John Smith via Your Company <ycompany@example.com>
    """
    @api.model
    def _get_default_from(self):

        # Check settings. If not using company email fallback to original function
        user = self.env.user
        company = user.company_id

        if not company.use_company_email:
            if user.email:
                return formataddr((user.name, user.email))
            raise UserError(_("Unable to send email, please configure the sender's email address."))

        if company.email:
            if company.add_company_from:
                if company.email_joint:
                    name_from = '%s %s %s' % (user.name, company.email_joint, company.name)
                else:
                    name_from = '%s %s' % (user.name, company.name)
            else:
                name_from = user.name

            return formataddr((name_from, company.email))

        raise UserError(_("Unable to send email, please configure company email address."))

    # Fields
    email_from = fields.Char(default=_get_default_from)

###############
# Mail.Thread #
###############
class PRTMailThread(models.AbstractModel):
    _name = "mail.thread"
    _inherit = "mail.thread"

    """
     Check settings and use company's email if forced.
     Make 'Reply-to:' look like 'John Smith via Your Company <yourcompany@example.com>
     Code of the function mostly taken from original addon, so need to check if it modified in original source.
     """

    @api.model
    def message_get_reply_to(self, res_ids, default=None):
        """ Returns the preferred reply-to email address that is basically the
        alias of the document, if it exists. Override this method to implement
        a custom behavior about reply-to for generated emails. """

        # Check settings. If not using company email fallback to original function
        if not self.env.user.company_id.add_sender_reply_to:
            return super(PRTMailThread, self).message_get_reply_to(res_ids, default)

        model_name = self.env.context.get('thread_model') or self._name
        alias_domain = self.env['ir.config_parameter'].sudo().get_param("mail.catchall.domain")
        res = dict.fromkeys(res_ids, False)

        # alias domain: check for aliases and catchall
        aliases = {}
        doc_names = {}
        if alias_domain:
            if model_name and model_name != 'mail.thread' and res_ids:
                mail_aliases = self.env['mail.alias'].sudo().search([
                    ('alias_parent_model_id.model', '=', model_name),
                    ('alias_parent_thread_id', 'in', res_ids),
                    ('alias_name', '!=', False)])
                # take only first found alias for each thread_id, to match
                # order (1 found -> limit=1 for each res_id)
                for alias in mail_aliases:
                    if alias.alias_parent_thread_id not in aliases:
                        aliases[alias.alias_parent_thread_id] = '%s@%s' % (alias.alias_name, alias_domain)
                doc_names.update(
                    dict((ng_res[0], ng_res[1])
                         for ng_res in self.env[model_name].sudo().browse(aliases).name_get()))
            # left ids: use catchall
            left_ids = set(res_ids).difference(set(aliases))
            if left_ids:
                catchall_alias = self.env['ir.config_parameter'].sudo().get_param("mail.catchall.alias")
                if catchall_alias:
                    aliases.update(dict((res_id, '%s@%s' % (catchall_alias, alias_domain)) for res_id in left_ids))

            # Compose name for 'reply-to'
            user = self.env.user
            company = user.company_id
            if company.add_sender_reply_to:
                if company.email_joint:
                    company_name = '%s %s %s' % (user.name, company.email_joint, company.name)
                else:
                    company_name = '%s %s' % (user.name, company.name)
            else:
                company_name = company.name

            for res_id in aliases:
                email_name = '%s%s' % (company_name, doc_names.get(res_id) and (' ' + doc_names[res_id]) or '')
                email_addr = aliases[res_id]
                res[res_id] = formataddr((email_name, email_addr))
        left_ids = set(res_ids).difference(set(aliases))
        if left_ids:
            res.update(dict((res_id, default) for res_id in res_ids))
        return res


###############
# Res.Company #
###############
class PRTResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    use_company_email = fields.Boolean(string="Use Company Email",
                                       help="Before: 'Some User <some.user@example.com>'\n"
                                            "After: Some User <mycompany@example.com>")
    add_company_from = fields.Boolean(string="Company Name In 'From'",
                                      help="Before: 'Some User <mycompany@example.com>'\n"
                                           "After: Some User via My Company <mycompany@example.com>")
    add_sender_reply_to = fields.Boolean(string="Sender's Name In 'Reply-to'",
                                         help="Before: 'My Company <mycompany@example.com>'\n"
                                              "After: Some User via My Company <mycompany@example.com>")
    email_joint = fields.Char(string="Name Joint", translate=True, default='via',
                              help="Before: 'Some User My Company <mycompany@example.com>'\n"
                                   "After: Some User via My Company <mycompany@example.com>")
