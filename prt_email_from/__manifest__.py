# -*- coding: utf-8 -*-
{
    'name': 'Email Fields Tweaks: Company email as Sender address, add Company name to From, add Sender name to Reply-to.'
            ' Recipients now can reply to message back in Odoo instead of sending reply to private address',
    'version': '11.0.1.2',
    'summary': """Customize 'from' and 'reply-to' addresses for email messages sent from Odoo""",
    'author': 'Ivan Sokolov',
    'category': 'Productivity',
    'license': 'GPL-3',
    'website': 'https://demo.promintek.com',
    'description': """
    Use company email address for outgoing email messages (Some User <some.user@example.com> / Some User <mycompany@example.com>)_\n
    Add company name to sender's name in 'From' (Some User <mycompany@example.com> / Some User via My Company <mycompany@example.com>)\n
    Add sender's name to company name in 'Reply-to' (My Company <mycompany@example.com> / Some User via My Company <mycompany@example.com>)\n
    Set names joint for 'From' and 'Reply-to' (Some User My Company <mycompany@example.com> / Some User via My Company <mycompany@example.com>)\n              
""",
    'depends': ['base', 'mail'],
    'images': ['static/description/banner.png'],

    'data': [
        'views/res_company.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
