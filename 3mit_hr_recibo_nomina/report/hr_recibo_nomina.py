from odoo import models, api, _, exceptions
from datetime import datetime, date, timedelta


class ReportAccountPayment(models.AbstractModel):
    _name = 'report.3mit_hr_recibo_nomina.template_recibo_nomina'

    @api.model
    def _get_report_values(self, docids, data=None):
        payslip_module = self.env['hr.payslip'].search([('id', '=', docids)])
        datos_factura = []
        asignaciones = []
        deducciones = []

        if payslip_module.state == 'draft':
            raise exceptions.except_orm(_('Advertencia!'), (
                "No se puede imprimir un reporte que no se encuentre en estado Realizado"))

        for slip in payslip_module:
            # DATOS DEL TRABAJADOR
            employee_name = slip.employee_id.display_name
            employee_ci = slip.employee_id.identification_id_2
            employee_nationality = slip.employee_id.nationality
            employee_rif = slip.employee_id.rif
            employee_job = slip.employee_id.job_id.display_name
            employee_week_salary = 0
            employee_daily_salary = 0

            # DATOS DEL EMPLEADOR
            employer_name = slip.employee_id.coach_id.display_name
            employer_ci = slip.employee_id.coach_id.identification_id_2
            employer_nationality = slip.employee_id.coach_id.nationality

            # FECHA DE INGRESO DEL EMPLEADO
            employee_start_date = slip.employee_id.fecha_inicio
            employee_fecha_ingreso = ' '
            if employee_start_date:
                employee_fecha_ingreso = employee_start_date.strftime("%d") + "/" + employee_start_date.strftime(
                    "%m") + "/" + employee_start_date.strftime(
                    "%Y")

            # FECHA DE INICIO DEL RECIBO
            receipt_date1 = slip.date_from
            receipt_date_from = ' '
            if receipt_date1:
                receipt_date_from = receipt_date1.strftime("%d") + "/" + receipt_date1.strftime(
                    "%m") + "/" + receipt_date1.strftime(
                    "%Y")

            # FECHA DE CIERRE DEL RECIBO
            receipt_date2 = slip.date_to
            receipt_date_to = ' '
            if receipt_date2:
                receipt_date_to = receipt_date2.strftime("%d") + "/" + receipt_date2.strftime(
                    "%m") + "/" + receipt_date2.strftime("%Y")

            # FECHA DE EMISIÓN DEL RECIBO
            today = date.today()
            receipt_date = ' '
            if today:
                receipt_date = today.strftime("%d") + "/" + today.strftime(
                    "%m") + "/" + today.strftime("%Y")

            # DATOS RECIBO
            total_deducciones = 0
            employee_basic_salary = 0

            if not slip.line_ids:
                raise exceptions.except_orm(_('Advertencia!'), (
                    "Por favor verifique si tiene cargado los conceptos de la Estructura Salarial "))

            n_dias = slip.worked_days_line_ids[0].number_of_days
            valor_diario = ""
            if n_dias > 30:
                n_dias = 30

            # SALARIO BASICO, SEMANAL Y DIARIO
            for a in slip.line_ids:
                if a.category_id.code == 'BASIC':
                    employee_basic_salary = a.total
                    employee_daily_salary = employee_basic_salary/n_dias
                    employee_week_salary = employee_daily_salary * 7

            for a in slip.line_ids:
                porcentaje = ' '
                monto = a.total
                if a.category_id.code == 'ALW' or a.category_id.code == 'BASIC':
                    if monto != 0:
                        valor_diario = monto / n_dias
                        valor_diario = '{0:,.2f}'.format(valor_diario).replace(',', 'X').replace('.', ',').replace('X','.')

                        asignaciones.append({
                            'descripcion': a.name,
                            'total_alw': '{0:,.2f}'.format(monto).replace(',', 'X').replace('.', ',').replace('X','.'),
                            'total_ded': ' ',
                            'cant_sueldo': int(n_dias),
                            'unidad': valor_diario,
                        })

                if a.category_id.code == 'DED':
                    if monto:
                        porcentaje = -((a.total * 100) / employee_basic_salary)
                        porcentaje = '{0:,.2f}'.format(porcentaje).replace('.', ',')
                        porcentaje = porcentaje + '%'
                        total_deducciones += monto

                    deducciones.append({
                        'descripcion': a.name,
                        'total_alw': ' ',
                        'total_ded': '{0:,.2f}'.format(monto).replace(',', 'X').replace('.', ',').replace('X', '.'),
                        'porcentaje': porcentaje,
                    })

                if a.category_id.code == 'GROSS':
                    total_asignaciones = a.total
                if a.category_id.code == 'NET':
                    suma_neta = a.total

            datos_factura.append({
                # DATOS DEL EMPLEADO
                'name': employee_name,
                'cargo': employee_job,
                'rif': employee_rif,
                'cedula': employee_ci,
                'fecha_ingreso': employee_fecha_ingreso,
                'letra_cedula': employee_nationality,
                'salario_diario': employee_daily_salary,

                # DATOS DEL RECIBO
                'date_from': receipt_date_from,
                'date_to': receipt_date_to,
                'fecha_genera': receipt_date,

                # DATOS DEL EMPLEADOR
                'empleador': employer_name,
                'cedula_res': employer_ci,
                'letra_cedula2': employer_nationality,
            })

        return {
            'data': data,
            'model': self.env['report.3mit_hr_recibo_nomina.template_recibo_nomina'],
            'datos_factura': datos_factura,
            'asignaciones': asignaciones,
            'deducciones': deducciones,
            'total_asignaciones': total_asignaciones,
            'total_deducciones': total_deducciones,
            'suma_neta' : suma_neta,
            'salario_diario': '{0:,.2f}'.format(employee_daily_salary).replace(',', 'X').replace('.', ',').replace('X', '.'),
            'salario_semanal': '{0:,.2f}'.format(employee_week_salary).replace(',', 'X').replace('.', ',').replace('X', '.'),
        }
