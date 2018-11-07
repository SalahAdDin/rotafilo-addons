{
    'name': 'MRP Bom Line Measures',
    'version': '11.0',
    'author': 'José Luis Sandoval Alaguna',
    'website': '',
    'category': 'Manufacture',
    'sequence': 15,
    'summary': 'Add engineering fields to BoM and Manufacturing issues.',
    'images': [],
    'depends': [
        'mrp',
        'stock',
        'purchase',
        'sale_stock',
    ],
    'description': """
MRP Bom Line Measures
=====================
Manage measures for items in Product's BoM.
    """,
    'data': [
        'views/mrp_bom_lines.xml',
        'views/purchase_views.xml',
        'report/mrp_bom_structure_report_templates.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
