{
    'name': 'Mail Inform Purchase',
    'version': '11.0',
    'summary': 'Send a mail with purchase information to the CEO.',
    'description': """
Mail Inform Purchase
====================
    """,
    'category': 'Tools',
    'author': 'José Luis Sandoval Alaguna',
    'website': '',
    'license': '',
    'depends': [
        'mail',
        'purchase'
    ],
    'data': [
        'data/mail_template_data.xml',
        'views/purchase_views.xml',
    ],
    'demo': [''],
    'installable': True,
    'auto_install': False,
}
