# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Reporte Recibo de Nomina',
    'version' : '2.0',
    'summary': 'Generate payroll receipt report',
    'sequence': 30,
    'description': """
    This module generates a payroll receipt report for INTELECTRA company
    Colaboradores: María Carreño 
    """,

    'category': 'Human Resources',
    'website': 'http://www.3MIT.com',
    'depends' : ['hr_payroll', '3mit_hr_datos_rrhh', 'hr_personal_info'],
    'data': [
        'report/hr_recibo_nomina.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}