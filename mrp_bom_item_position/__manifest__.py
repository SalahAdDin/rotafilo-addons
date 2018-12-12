{
    'name': 'MRP Bom Item Position',
    'version': '11.0',
    'author': 'José Luis Sandoval Alaguna',
    'website': '',
    'category': 'Manufacture',
    'sequence': 15,
    'summary': 'Add the engineering CAD item position field to BoM lines.',
    'images': [],
    'depends': [
        'mrp',
        'mrp_variant_configurator',
    ],
    'description': """
MRP Bom Item Position
=====================
Add the engineering CAD item position field to BoM lines.
    """,
    'data': [
        'views/mrp_bom_lines.xml',
        'report/mrp_bom_structure_report_templates.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
