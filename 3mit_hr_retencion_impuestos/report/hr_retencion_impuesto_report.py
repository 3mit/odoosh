# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time

from datetime import datetime, date, timedelta, time
from odoo import models, fields, api,exceptions, _

class hr_retencion_report(models.TransientModel):
    _name = 'hr.retencion.report'
    _description = 'Historico de retenciones'

    date_from = fields.Date('Date From')
    date_to = fields.Date('date_to')
    empleado = fields.Many2one('hr.employee')

    def print_report(self):
        update = {'empleado': self.empleado.id, 'date_from': self.date_from, 'date_to': self.date_to}
        return self.env.ref('int_hr_retencion_impuestos.action_hr_report_retencion_reporte').report_action([], data=update)

class ReportAccountPayment_5(models.AbstractModel):
    _name = 'report.int_hr_retencion_impuestos.template_retencion_report'

    @api.model
    def _get_report_values(self, docids, data):
        empleado = self.env['hr.employee'].search([('id','=',data['empleado'])])
        res = dict()
        docs = []
        docs2 = []
        date_from = data['date_from']
        date_to =  data['date_to']
        slips = self.env['hr.payslip'].search([('employee_id','=',data['empleado']),('date_from','>=', date_from),('date_to','<=',date_to),('state','=','done')])
        monto_islr_enero = monto_islr_febrero = monto_islr_marzo = monto_islr_abril = monto_islr_mayo = monto_islr_junio = monto_islr_julio = monto_islr_agosto = monto_islr_septiembre = monto_islr_octubre = monto_islr_noviembre = monto_islr_diciembre = 0.0
        salario_enero = salario_febrero =  salario_marzo = salario_abril = salario_mayo = salario_junio = salario_julio = salario_agosto = salario_septiembre = salario_octubre = salario_noviembre = salario_diciembre = 0.0
        porcentaje_enero = porcentaje_febrero = porcentaje_marzo = porcentaje_abril = porcentaje_mayo = porcentaje_junio = porcentaje_julio = porcentaje_agosto = porcentaje_septiembre = porcentaje_octubre = porcentaje_noviembre = porcentaje_diciembre = 0.0

        if date_from:
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
            date_from = date_from.strftime('%d/%m/%Y')
        if date_to:
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
            date_to = date_to.strftime('%d/%m/%Y')
        beneficiario_direccion = str(empleado.state_id_res.name) + ' ' + str(empleado.city_id_res.name)+ ' ' + str(empleado.e_municipio.name)+ ' ' + str(empleado.e_parroquia.name)+ ' ' + str(empleado.code_postal)+ ' ' + str(empleado.street)+ ' ' + str(empleado.house)+ ' ' + str(empleado.apto)+ ' ' + str(empleado.piso)
        beneficiario_direccion = beneficiario_direccion.replace("False",'')
        for slip in slips:
            if slip.date_to.strftime("%m") == '01':
                mes = 'ENERO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_enero += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_enero += slip.line_ids.total
                if salario_enero == 0:
                    porcentaje_enero = 0.0
                else:
                    porcentaje_enero = (monto_islr_enero*100)/salario_enero

            if slip.date_to.strftime("%m") == '02':
                mes = 'FEBRERO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_febrero += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_febrero += slip.line_ids.total
                if salario_febrero == 0:
                    porcentaje_febrero = 0.0
                else:
                    porcentaje_febrero = (monto_islr_febrero*100)/salario_febrero

            if slip.date_to.strftime("%m") == '03':
                mes = 'MARZO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_marzo += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_marzo += slip.line_ids.total
                if salario_marzo == 0:
                    porcentaje_marzo = 0.0
                else:
                    porcentaje_marzo = (monto_islr_marzo*100)/salario_marzo

            if slip.date_to.strftime("%m") == '04':
                mes = 'ABRIL'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_abril += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_abril += slip.line_ids.total
                if salario_abril == 0:
                    porcentaje_abril = 0.0
                else:
                    porcentaje_abril = (monto_islr_abril*100)/salario_abril

            if slip.date_to.strftime("%m") == '05':
                mes = 'MAYO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_mayo += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_mayo += slip.line_ids.total
                if salario_mayo == 0:
                    porcentaje_mayo = 0.0
                else:
                    porcentaje_mayo = (monto_islr_mayo*100)/salario_mayo

            if slip.date_to.strftime("%m") == '06':
                mes = 'JUNIO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_junio += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_junio += slip.line_ids.total
                if salario_junio == 0:
                    porcentaje_junio = 0.0
                else:
                    porcentaje_junio = (monto_islr_junio*100)/salario_junio

            if slip.date_to.strftime("%m") == '07':
                mes = 'JULIO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_julio += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_julio += slip.line_ids.total
                if salario_julio == 0:
                    porcentaje_julio = 0.0
                else:
                     porcentaje_julio = (monto_islr_julio*100)/salario_julio

            if slip.date_to.strftime("%m") == '08':
                mes = 'AGOSTO'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_agosto += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_agosto += slip.line_ids.total
                if salario_agosto == 0:
                    porcentaje_agosto = 0.0
                else:
                     porcentaje_agosto = (monto_islr_agosto*100)/salario_agosto

            if slip.date_to.strftime("%m") == '09':
                mes = 'SEPTIEMBRE'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_septiembre += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_septiembre += slip.line_ids.total
                if salario_septiembre == 0:
                    porcentaje_septiembre = 0.0
                else:
                    porcentaje_septiembre = (monto_islr_septiembre*100)/salario_septiembre

            if slip.date_to.strftime("%m") == '10':
                mes = 'OCTUBRE'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_octubre += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_octubre += slip.line_ids.total
                    if salario_octubre == 0:
                        porcentaje_octubre = 0.0
                    else:
                        porcentaje_octubre = (monto_islr_octubre*100)/salario_octubre

            if slip.date_to.strftime("%m") == '11':
                mes = 'NOVIEMBRE'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_octubre += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_octubre += slip.line_ids.total
                    if salario_octubre == 0:
                        porcentaje_octubre = 0.0
                    else:
                        porcentaje_octubre = (monto_islr_octubre * 100) / salario_octubre

            if slip.date_to.strftime("%m") == '12':
                mes = 'DICIEMBRE'
                for regla in slip.line_ids.salary_rule_id:
                    if regla.amount_python_compute.find("contract.islr_withholding_value/100") != -1:
                        monto_islr_diciembre += slip.line_ids.total
                    if regla.amount_python_compute.find("((contract.wage / 4)/7)*(worked_days.WORK100.number_of_days)") != -1:
                        salario_diciembre += slip.line_ids.total
                if salario_diciembre == 0:
                    porcentaje_diciembre = 0.0
                else:
                    porcentaje_diciembre = (monto_islr_diciembre*100)/salario_diciembre

        impuesto_enero = monto_islr_enero
        remuneracion_enero = salario_enero

        impuesto_febrero = monto_islr_febrero + monto_islr_enero
        remuneracion_febrero = salario_febrero + salario_enero

        impuesto_marzo = monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_marzo = salario_marzo + salario_febrero + salario_enero

        impuesto_abril = monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_abril = salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_mayo = monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_mayo = salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_junio = monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_junio = salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_julio = monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_julio = salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_agosto = monto_islr_agosto + monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_agosto = salario_agosto + salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_septiembre = monto_islr_septiembre + monto_islr_agosto + monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_septiembre = salario_septiembre + salario_agosto + salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_octubre = monto_islr_octubre + monto_islr_septiembre + monto_islr_agosto + monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_octubre = salario_octubre + salario_septiembre + salario_agosto + salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_noviembre = monto_islr_noviembre + monto_islr_octubre + monto_islr_septiembre + monto_islr_agosto + monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_noviembre = salario_noviembre + salario_octubre + salario_septiembre + salario_agosto + salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        impuesto_diciembre =  monto_islr_diciembre + monto_islr_noviembre + monto_islr_octubre + monto_islr_septiembre + monto_islr_agosto + monto_islr_julio + monto_islr_junio + monto_islr_mayo + monto_islr_abril + monto_islr_marzo + monto_islr_febrero + monto_islr_enero
        remuneracion_diciembre = salario_diciembre + salario_noviembre  + salario_octubre + salario_septiembre + salario_agosto + salario_julio + salario_junio + salario_mayo + salario_abril + salario_marzo  + salario_febrero + salario_enero

        porcentaje_enero = round(porcentaje_enero,2)
        porcentaje_febrero = round(porcentaje_febrero, 2)
        porcentaje_marzo = round(porcentaje_marzo, 2)
        porcentaje_abril = round(porcentaje_abril, 2)
        porcentaje_mayo = round(porcentaje_mayo, 2)
        porcentaje_junio = round(porcentaje_junio, 2)
        porcentaje_julio = round(porcentaje_julio, 2)
        porcentaje_agosto = round(porcentaje_agosto, 2)
        porcentaje_septiembre = round(porcentaje_septiembre, 2)
        porcentaje_octubre = round(porcentaje_octubre, 2)
        porcentaje_noviembre = round(porcentaje_noviembre, 2)
        porcentaje_diciembre = round(porcentaje_diciembre, 2)
        docs2.append({
            'salario_enero' : self.separador_cifra(salario_enero),
            'porcentaje_enero': self.separador_cifra(porcentaje_enero),
            'impuesto_enero': self.separador_cifra(monto_islr_enero),
            'acumulado_enero':self.separador_cifra(impuesto_enero),
            'remuneracion_enero': self.separador_cifra(remuneracion_enero),

            'salario_febrero': self.separador_cifra(salario_febrero),
            'porcentaje_febrero': self.separador_cifra(porcentaje_febrero),
            'impuesto_febrero': self.separador_cifra(monto_islr_febrero),
            'acumulado_febrero': self.separador_cifra(impuesto_febrero),
            'remuneracion_febrero': self.separador_cifra(remuneracion_febrero),

            'salario_marzo': self.separador_cifra(salario_marzo),
            'porcentaje_marzo': self.separador_cifra(porcentaje_marzo),
            'impuesto_marzo': self.separador_cifra(monto_islr_marzo),
            'acumulado_marzo': self.separador_cifra(impuesto_marzo),
            'remuneracion_marzo': self.separador_cifra(remuneracion_marzo),

            'salario_abril': self.separador_cifra(salario_abril),
            'porcentaje_abril': self.separador_cifra(porcentaje_abril),
            'impuesto_abril': self.separador_cifra(monto_islr_abril),
            'acumulado_abril': self.separador_cifra(impuesto_abril),
            'remuneracion_abril': self.separador_cifra(remuneracion_abril),

            'salario_mayo': self.separador_cifra(salario_mayo),
            'porcentaje_mayo': self.separador_cifra(porcentaje_mayo),
            'impuesto_mayo': self.separador_cifra(monto_islr_mayo),
            'acumulado_mayo': self.separador_cifra(impuesto_mayo),
            'remuneracion_mayo': self.separador_cifra(remuneracion_mayo),

            'salario_junio': self.separador_cifra(salario_junio),
            'porcentaje_junio': self.separador_cifra(porcentaje_junio),
            'impuesto_junio': self.separador_cifra(monto_islr_junio),
            'acumulado_junio': self.separador_cifra(impuesto_junio),
            'remuneracion_junio': self.separador_cifra(remuneracion_junio),

            'salario_julio': self.separador_cifra(salario_julio),
            'porcentaje_julio': self.separador_cifra(porcentaje_julio),
            'impuesto_julio': self.separador_cifra(monto_islr_julio),
            'acumulado_julio': self.separador_cifra(impuesto_julio),
            'remuneracion_julio': self.separador_cifra(remuneracion_julio),

            'salario_agosto': self.separador_cifra(salario_agosto),
            'porcentaje_agosto': self.separador_cifra(porcentaje_agosto),
            'impuesto_agosto': self.separador_cifra(monto_islr_agosto),
            'acumulado_agosto': self.separador_cifra(impuesto_agosto),
            'remuneracion_agosto': self.separador_cifra(remuneracion_agosto),

            'salario_septiembre': self.separador_cifra(salario_septiembre),
            'porcentaje_septiembre': self.separador_cifra(porcentaje_septiembre),
            'impuesto_septiembre': self.separador_cifra(monto_islr_septiembre),
            'acumulado_septiembre': self.separador_cifra(impuesto_septiembre),
            'remuneracion_septiembre': self.separador_cifra(remuneracion_septiembre),

            'salario_octubre': self.separador_cifra(salario_octubre),
            'porcentaje_octubre': self.separador_cifra(porcentaje_octubre),
            'impuesto_octubre': self.separador_cifra(monto_islr_octubre),
            'acumulado_octubre': self.separador_cifra(impuesto_octubre),
            'remuneracion_octubre': self.separador_cifra(remuneracion_octubre),

            'salario_noviembre': self.separador_cifra(salario_noviembre),
            'porcentaje_noviembre': self.separador_cifra(porcentaje_noviembre),
            'impuesto_noviembre': self.separador_cifra(monto_islr_noviembre),
            'acumulado_noviembre': self.separador_cifra(impuesto_noviembre),
            'remuneracion_noviembre': self.separador_cifra(remuneracion_noviembre),

            'salario_diciembre': self.separador_cifra(salario_diciembre),
            'porcentaje_diciembre': self.separador_cifra(porcentaje_diciembre),
            'impuesto_diciembre': self.separador_cifra(monto_islr_diciembre),
            'acumulado_diciembre': self.separador_cifra(impuesto_diciembre),
            'remuneracion_diciembre': self.separador_cifra(remuneracion_diciembre),
        })

        if empleado.address_id.zip:
            employee_zip = ',' +  ' ' + 'Zona Postal' + ' '+  str(empleado.address_id.zip)
        else:
            employee_zip = ' '
        compañia = str(empleado.address_id.street) + ',' + ' ' + str(empleado.address_id.street2) + ',' + ' ' + str(empleado.address_id.state_id.name) + ','  + ' ' + str(empleado.address_id.city) + employee_zip
        compañia = compañia.replace('False,', ' ')
        compañia = compañia.replace('False', ' ')

        docs.append({
            'date_from': date_from,
            'date_to': date_to,
            'agente_razon': empleado.address_id.name,
            'agente_rif': empleado.address_id.vat,
            'agente_direccion': compañia,
            'beneficiario_nombre': empleado.name,
            'beneficiario_rif': empleado.rif,
            'beneficiario_cedula': empleado.identification_id_2,
            'beneficiario_direccion': beneficiario_direccion,

        })

        return {
            'model': self.env['report.int_hr_retencion_impuestos.template_retencion_report'],
            'lines': res,
            'docs': docs,
            'docs2':docs2,

        }

    def numero_to_letras(self,numero):
        indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
        entero = int(numero)
        contador = 0
        numero_letras = ""
        while entero > 0:
            a = entero % 1000
            if contador == 0:
                en_letras = self.convierte_cifra(a, 1).strip()
            else:
                en_letras = self.convierte_cifra(a, 0).strip()
            if a == 0:
                numero_letras = en_letras + " " + numero_letras
            elif a == 1:
                if contador in (1, 3):
                    numero_letras = indicador[contador][0] + " " + numero_letras
                else:
                    numero_letras = en_letras + " " + indicador[contador][0] + " " + numero_letras
            else:
                numero_letras = en_letras + " " + indicador[contador][1] + " " + numero_letras
            numero_letras = numero_letras.strip()
            contador = contador + 1
            entero = int(entero / 1000)
        numero_letras = numero_letras
        return numero_letras
    def convierte_cifra(self,numero, sw):
        lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS",
                         "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
        lista_decena = ["", (
        "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"),
                        ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y "), ("CUARENTA", "CUARENTA Y "),
                        ("CINCUENTA", "CINCUENTA Y "), ("SESENTA", "SESENTA Y "),
                        ("SETENTA", "SETENTA Y "), ("OCHENTA", "OCHENTA Y "),
                        ("NOVENTA", "NOVENTA Y ")
                        ]
        lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
        centena = int(numero / 100)
        decena = int((numero - (centena * 100)) / 10)
        unidad = int(numero - (centena * 100 + decena * 10))
        # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

        texto_centena = ""
        texto_decena = ""
        texto_unidad = ""

        # Valida las centenas
        texto_centena = lista_centana[centena]
        if centena == 1:
            if (decena + unidad) != 0:
                texto_centena = texto_centena[1]
            else:
                texto_centena = texto_centena[0]

        # Valida las decenas
        texto_decena = lista_decena[decena]
        if decena == 1:
            texto_decena = texto_decena[unidad]
        elif decena > 1:
            if unidad != 0:
                texto_decena = texto_decena[1]
            else:
                texto_decena = texto_decena[0]
        # Validar las unidades
        # print "texto_unidad: ",texto_unidad
        if decena != 1:
            texto_unidad = lista_unidad[unidad]
            if unidad == 1:
                texto_unidad = texto_unidad[sw]

        return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)

    def separador_cifra(self,valor):
        monto = '{0:,.2f}'.format(valor).replace('.', '-')
        monto = monto.replace(',', '.')
        monto = monto.replace('-', ',')
        return  monto