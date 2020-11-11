
{
    'name': 'Datos de RRHH',
    'version': '1.0',
    'author': 'TYSAMNCA',
    'category': 'Human Resources',
    'sequence': 103,
    'summary': 'Show human resources data',
    'description': u'''
        Agrega la pestaña Datos RRHH a la ficha del empleado, con los siguientes campos.\n
            * Información Adicional
                * Fecha de Ingreso
                * Fecha de Egreso
                * Motivo de Egreso
            * Antigüedad
                * Días
                * Meses
                * Años
            * Información Bancaria
                * Institución Financiera
                * Nro. de Cuenta
            * Tipo de Cuenta
    ''',
    'depends': [
        'base_setup',
        'hr',
        'hr_egress_conditions',
        'hr_localization_permisology',
    ],
    'data': [
        'views/hr_datos_rrhh_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
