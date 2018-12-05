# Copyright 2017 Jose Luis Sandoval Alaguna <jose.alaguna@rotafilo.com.tr>
{
    'name': 'MRP - Product variants',
    'version': '11.0.1.0.1',
    'summary': 'Product variants in MRP management',
    'description': '',
    'category': 'Manufacturing',
    'author': 'José Luis Sandoval Alaguna - Rotafilo',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        "mrp",
        "product_variant_configurator",
    ],
    'data': [
        'views/mrp_bom_lines.xml',
    ],
    'installable': True,
    'auto_install': False,
    "post_init_hook": "assign_product_template",
}
