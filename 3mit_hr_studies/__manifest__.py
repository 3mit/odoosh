# -*- coding: utf-8 -*-
#    Create:  jeeduardo** 28/04/2016 **  **
#    type of the change:  Creacion
#    Comments: Creacion del modulo de hr_salary_rule_direct_account
# 'views/hr_salary_rule_view.xml',
# -----------------------------------------------------------------------------
#    Modified by: k-pérez 2020/10/01
#    Type of change: migration v11 to v13
#    Comments: Field validations, removed unused statements, refactor, class changed to CamelCase.
# -----------------------------------------------------------------------------
{
    'name': '3mit_hr_studies',

    'summary': """
        Este módulo fue diseñado para añadir información acerca de los estudios y 
        la información académica de sus empleados.""",

    'description': '''
    \nAñade distintos campos:
    \n1) información acerca de los cursos realizados.
    \n2) Información sobre la carrera académica que posee actualmente.
    \n3) EL nivel relacionado a los lenguajes que puede hablar y/o dominar.

''',
    'author': ['3MIT', 'kPérez'],
    'category': 'Human Resources',
    'version': '1.1.1',
    'data': [
            'security/ir.model.access.csv',
            'view/studies_view.xml'
        ],
    'depends': ['base', 'hr'],
    'installable': True,

}
