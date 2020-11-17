# coding: utf-8
##############################################################################
#
# Copyright (c) 2016 Tecnología y Servicios AMN C.A. (http://3MIT.com/) All Rights Reserved.
# <contacto@3MIT.com>
# <Teléfono: +58(212) 237.77.53>
# Caracas, Venezuela.
#
# Colaborador: <<nombre colaborador>> <e-mail del colaborador>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    'name': 'Nómina de liquidaciones',
    'version': '13.0',
    'category': 'Recursos Humanos',
    'summary': 'Permite generar la liquidacion para los empleados',
    'description': """
Nómina de Liquidaciones
==================================

Permite generar las nominas de liquidacion de los empleados

    Elaborated by Yorman Pineda.
    """,

    'author': '3MIT',
    'website': 'https://3MIT.com',
    'depends': ['3mit_hr_payroll','3mit_hr_special_payroll','3mit_hr_config_parameter','3mit_hr_contract_add_fields', 'hr_payroll_account', '3mit_hr_egress_conditions'],
    'data': ['views/hr_payroll_payoff_view.xml',],
    #'demo': [],
    #'test': [],
    'installable': True

}
