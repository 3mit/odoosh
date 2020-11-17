# coding: utf-8
##############################################################################
#
# Copyright (c) 2016 Tecnología y Servicios AMN C.A. (http://3MIT.com/) All Rights Reserved.
# <contacto@3MIT.com>
# <Teléfono: +58(212) 237.77.53>
# Caracas, Venezuela.
#
# Colaborador: <<Kleiver Pérez>> <kleiver@3mit.dev>
#
##############################################################################

{
    'name': 'Nóminas Especiales',
    'version': '2',
    'category': 'Recursos Humanos',
    'summary': 'Agrega funcionalidades comunes para el cálculo de las nóminas especiales',
    'description': """
NÓMINAS ESPECIALES
Colaborador: Kleiver Pérez.
=========================================================================

\nAgrega funcionalidades comunes para el cálculo de las nóminas especiales:

    * Cálculo del tiempo de servicio del empleado.
    * Cálculo del sueldo promedio.
    * Cálculo de alícuota de bono vacacional.
    * Cálculo de alícuota de utilidades.

    """,

    'author': '3MIT',
    'depends': ['hr', 'hr_payroll', 'hr_contract', '3mit_hr_special_days'],
    'data': ['views/hr_special_payroll_view.xml',
             'security/ir.model.access.csv',
             'data/hr_special_payroll_data.xml'
             ],
    # 'demo': [],
    # 'test': [],
    'installable': True,
}
