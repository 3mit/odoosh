# coding: utf-8
############################################################################################################
#
#    Modified by: k-pérez 2020/11/10.
#    Type of change: migration v11 to v13.
#    Comments: Field validations, removed unused statements, refactor, class changed to CamelCase.
#
############################################################################################################
{
    "name": "Nómina: Días Especiales",
    "version": "8.0.0.0.6",
    "author": ["3MIT", "Kleiver Pérez", "Dieg Marfil"],
    "category": "Human Resource",

    "depends": [
        "base",
        "hr_payroll",
        "hr_holidays",
        '3mit_hr_localization_permisology',
    ],
    "data": [
        "views/hr_special_days.xml",
        'security/ir.model.access.csv',
    ],

    "installable": True,
    "auto_install": False,
}
