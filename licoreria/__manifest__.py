# -*- coding: utf-8 -*-
{
    'name': "Licoreria",

    'summary': """
        Este modulo sirve para gestionar los productos de una licoreria
     """,

    'description': """
        Este modulo sirve para gestionar los productos de una licoreria 
        para ello cuenta con dos tablas: Categoria Y Bebida que ayudaran
        a la debida gestión
    """,

    'author': "Jonathan Gonzalez Fraga",
    'website': "https://jonathangonzalezfraga.blogspot.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventario Alcohol',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',    
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml', 

    ],
    # only loaded in demonstration mode
    # 'reports/report_bebida.xml',
    'demo': [
        'demo/demo.xml',
    ],
}
