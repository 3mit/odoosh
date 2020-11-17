# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Datos Familiares',
    'version': '1.1',
    'author': '3MIT',
    'category': 'Human Resources',
    'sequence': 102,
    'summary': 'Show fields for Family data',
    'description': '''
        Show fields for Family data
    ''',
    'depends': [
        'base_setup',
        'hr',
    ],
    'data': [
        'views/hr_datos_familiares_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}