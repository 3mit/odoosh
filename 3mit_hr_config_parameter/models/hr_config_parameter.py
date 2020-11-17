# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import models, api, fields, _
from odoo.tools import ormcache
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HrSalaryRuleParameterValue(models.Model):
    _inherit = "hr.rule.parameter.value"

    name = fields.Char(related="rule_parameter_id.name", index="true", store=True, readonly=True)


HrSalaryRuleParameterValue()


class HrSalaryRuleParameter(models.Model):
    _inherit = "hr.rule.parameter"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('_unique', 'Check(1=1)', "El atributo ya existe."),
        ('name_unique', 'unique(name)', "Dos reglas en los parámetros no pueden contener el mismo nombre."),
    ]

    @api.model
    @ormcache('name', 'tuple(self.env.context.get("allowed_company_ids", []))')
    def _get_parameter_from_name(self, name):
        rule_parameter = self.env['hr.rule.parameter'].search([
            ('name', '=', name)], limit=1)
        if not rule_parameter:
            raise UserError(_("Ningún parámetro de regla con nombre '%s' ha sido encontrado") % name)
        return rule_parameter.code


HrSalaryRuleParameter()
