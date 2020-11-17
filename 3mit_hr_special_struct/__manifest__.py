# -*- encoding: UTF-8 -*-
#    Create:  randara** 19/07/2016 **  **
#    type of the change:  New module.
#    Comments: Creación del módulo de hr_special_slip.
# -------------------------------------------------------------------------------------------------------------
#    Modified by: k-pérez 2020/10/23
#    Type of change: migration v11 to v13.
#    Comments: Field validations, removed unused statements, refactor, class changed to CamelCase.
# -------------------------------------------------------------------------------------------------------------
{
    'name': 'Estructura Nóminas Especiales',
    'version': '1.1',
    'author': '3MIT',
    'category': 'Human Resources',
    'depends': ["hr_payroll", "hr", "base", "3mit_hr_payroll"],
    'description': """

Modulo para Nominas Especiales.\n
==============================================\n
Colaboración:
Rafael A. Andara D\n
Kleiver J. Pérez \n
\n
Este módulo crea la funcionalidad de nominas especiales donde se pueden definir y configurar nominas de pago\n
no continuo y no especificado en el contrato.
\nEs util para nominas tipo:\n
    - Cestatiket\n
    - Liquidacion\n
    - Utilidades\n
    - Pago de Guarderias\n
    Entre otras.\n
    """,
    'data': ["views/hr_special_struct.xml",
             "security/ir.model.access.csv"
             ],
    'installable': True,

}
