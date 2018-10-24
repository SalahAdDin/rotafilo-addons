{
    'name': 'MRP Measure',
    'version': '11.0',
    'author': 'José Luis Sandoval Alaguna',
    'website': '',
    'category': 'Manufacture',
    'sequence': 15,
    'summary': '',
    'images': [],
    'depends': [
        'base',
        'purchase',
        'product',
        'mrp',
        'sale_stock'
    ],
    'description': """
Manage measures for items in Product's BoM.
==============================================
    """,
    'data': [
        'views/mrp_bom_lines.xml',
        'views/purchase_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
