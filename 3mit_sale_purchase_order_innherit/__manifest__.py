# coding: utf-8
###########################################################################

##############################################################################
{
    "name": "Correcciones ventas y compras; rif, tipo de documento y Documento de Identidad",
    "version": "1.0",
    'description': """
    """,
    "author": "Localizacion Venezolana",
    "license": "AGPL-3",
    "category": "ventas",
    #"website": "",
    "colaborador":"Maria Carreño",
    "depends": [
        "sale",
        "base",
        "base_vat",
        "3mit_validation_res_partner",
        "3mit_validation_rif_res_company"
    ],
    'demo': [
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/sale_order_innherit.xml',
        'views/purchase_order_innherit.xml',


    ],
    'test': [

    ],
    "installable": True,
    'application': True,
}
