# -*- encoding: UTF-8 -*-
#    Create:  jeduardo** 05/07/2016 **  **
#    type of the change:  Creacion
#    Comments: Creacion del modulo de hr_personal_info
# -----------------------------------------------------------------------------
#    Modified by: k-pérez 2020/10/13
#    Type of change: migration v11 to v13.
#    Comments: Field validations, removed unused statements, refactor, class changed to CamelCase.
# -----------------------------------------------------------------------------
{
    'name': 'HR Personal Info',

    'summary': """
        Este módulo fue diseñado para añadir todo tipo de información personal
        concerniente de sus empleados.""",

    
    'description': '''\
Agrega nuevos campos y funcionalidades a la ficha del empleado.
=================================================================

V1.1.2.\n
1) Agrega un filtro de busqueda en la vista tree de los empleados.\n
2) Agrega el campo Cedula de identidad en la vista tree de los empleados.\n
3) Agrega los siguientes campos a la ficha del empleado:\n
    * Cedula de identidad\n
    * Rif\n
    * Nacionalidad\n
    * Correo electronico personal\n
    * Nivel Educativo\n
    * Profesion\n
    * Pais de nacimiento\n
    * Estado de nacimiento\n
    * Ciudad de nacimiento\n
    * Edad del empleado\n
    * Certificado de matrimonio (si/no)\n
    * Estado civil (modificado)\n
    * Nro. de hijos\n
    * Grupo sanguineo\n
    * Factor RH\n
    * Av./Calle\n
    * Edif. Quinta o Casa\n
    * Piso\n
    * Nro. de apartamento\n
    * Estado de residencia\n
    * Ciudad de residencia\n
    * Telefono de habitacion\n
    * Telefono de contacto\n

''',
    'author': ['TYSAMNCA', 'kPérez'],
    'category': 'Human Resources',
    'version': '1.1.2',
    'data': [
        'security/ir.model.access.csv',
        'views/hr_personal_info_view.xml',
        ],
    'depends': ['hr', 'three_mit_l10n_ve'],
    'installable': True,

}
