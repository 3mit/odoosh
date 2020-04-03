# -*- coding: UTF-8 -*-

{
    "name": "RIF Company-Respartner Validaciones y agregación de campos sobre la compañia",
    "version": "1.0",
    "author": "Maria Carreño",
    'depends' : [
                 "base","base_vat","3mit_validation_res_partner"],
    "data": [
        'security/ir.model.access.csv',
        'views/3mit_validation_res_company_rif.xml',
	    'views/3mit_validation_res_partner.xml',
             ],
    'category': 'company',
    "description": """
    Modifica campo y realiza validaciones al vat(nif) y al email de la compañia; Modifica campo y realiza validaciones al vat(nif) y al email del partner cliente-proveedor.
    """,
    'installable': True,
    'application': True,
}
