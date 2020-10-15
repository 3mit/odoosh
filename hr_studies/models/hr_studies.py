# -*- coding: utf-8 -*-
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee Studies'

    active_studies = fields.Boolean('¿Estudia Actualmente?')
    career_id = fields.Many2one('hr.career', 'Carrera')
    institution_id = fields.Char("Institución", size=100)
    # lang_id = fields.Many2one('res.lang', 'Idiomas')
    languages = fields.Boolean(string="Languages")
    languages_id = fields.One2many('hr.languages', 'employee_id', 'Idiomas')
    courses = fields.Boolean(string="Cursos del empleado")
    courses_ids = fields.One2many('hr.course', 'employee_id', 'Cursos')
    studies = fields.Boolean(string="Estudios del empleado")
    studies_ids = fields.One2many('hr.studies', 'employee_id', 'Estudios')


class HrCarrera(models.Model):
    _name = 'hr.career'
    _description = 'Carrera Description'

    name = fields.Char('Nombre de la carrera', size=128, required=True, index=True)
    # employee_ids = fields.One2many('hr.employee', 'career_id', 'Employees')


class HrCurso(models.Model):
    _name = 'hr.course'
    _description = 'Descripción del curso'

    name_instituto = fields.Char(string='Nombre de la Institución', size=256)
    name_curso = fields.Char(string='Nombre del curso', size=256)
    name_titulo = fields.Char(string='Título o Certificado obtenido', size=256)
    duracion = fields.Char(string='Duración', size=60)
    graduado = fields.Boolean(string='¿Graduado?', defaults=False)
    date_culminacion = fields.Date(string='Fecha de Culminación')
    employee_id = fields.Many2one('hr.employee', 'Empleado', ondelete='cascade')


# _defaults = {
#    'graduado': False,
# }

class HrEstudio(models.Model):
    _name = 'hr.studies'
    _description = 'Estudios del empleado'

    name_nivel = fields.Selection([('educacion_basica', 'Educación Básica'),
                                   ('bachiller', 'Bachiller'),
                                   ('tecnico_medio', 'Técnico Medio'),
                                   ('tsu', 'T.S.U.'),
                                   ('universitario', 'Universitario'),
                                   ('licenciado', 'Licenciado'),
                                   ('maestria', 'Maestría'),
                                   ('doctorado', 'Doctorado'),
                                   ('postdoctorado', 'Postdoctorado')
                                   ],
                                  'Nivel Educativo')
    name_institute = fields.Char(string='Nombre del Colegio/Institución', size=256)
    a_aprobado = fields.Integer(string='Años Aprobados', size=256)
    si_graduado = fields.Boolean(string='¿Graduado?')
    fecha_culminacion = fields.Date(string='Fecha de Culminación')
    nombre_titulo = fields.Char('Titulo o Certificado obtenido')
    employee_id = fields.Many2one('hr.employee', 'Empleado', ondelete='cascade')


class HrLanguages(models.Model):
    _name = 'hr.languages'
    _description = 'Employee Languages'

    LEVELS = [('básico', 'Básico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')]
    lang_id = fields.Many2one('res.lang', 'Idiomas')
    writing = fields.Selection(LEVELS, string='Escritura')
    reading = fields.Selection(LEVELS, string='Lectura')
    pronunciation = fields.Selection(LEVELS, string='Pronunciación')
    listening = fields.Selection(LEVELS, string='Escucha')
    employee_id = fields.Many2one('hr.employee', 'Empleado', ondelete='cascade')
