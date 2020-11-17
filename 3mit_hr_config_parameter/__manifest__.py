# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# -----------------------------------------------------------------------------
#    Created by: Kleiver Pérez 2020/11/09
#    Type of change: hr.config.parameter data added and model migration from v11 to v13.
#    Comments: Field validations, constraints and data and added.
# -----------------------------------------------------------------------------

{
    'name': 'Configuración de parámetros',
    'version': '1.6',
    'author': '3MIT',
    'category': 'Human Resources',
    'summary': 'Parámetros para el módulo de Nómina',
    'description': """Permite modificar parámetros para el módulo de Nómina.\n
                   Colaborador: Kleiver Pérez""",
    'depends': [
        'hr_payroll'
    ],
    'data': [
        # 'views/hr_config_parameter_view.xml',
        'data/hr_config_parameter_data.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'qweb': [],
}
