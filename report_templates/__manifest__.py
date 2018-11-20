{
    'name': 'Rotafilo Report Templates',
    'version': '11.0.1',
    'summary': 'Report templates used in the system.',
    'description': """
Rotafilo Report Templates
=========================
Easier way to install the custom report templates in the system.
    """,
    'category': 'Reporting',
    'author': 'José Luis Sandoval Alaguna',
    'website': '',
    'license': '',
    'depends': [
        'purchase',
    ],
    'data': [
        'report/ir_qweb.xml',
        'report/mrp_bom_structure_report_templates.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml',
    ],
    'demo': [''],
    'installable': True,
    'auto_install': False,
}
