# -*- coding: UTF-8 -*-

{
    "name": "Validaciones y agregación de campos sobre el partner",
    "version": "1.0",
    "author": "Maria Carreño",
    'depends' : [#"hr",
                 "base","base_vat"],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner_people_type.xml',
        'views/docum_ident_res_partner.xml',
             ],
    'category': 'cliente-proveedor',
    "description": """
     Agrega el tipo de persona, y coloca el Documento de Identidad segun el tipo de persona y sus respectivos atributos
    """,
    'installable': True,
    'application': True,
}
