from odoo import models, api, _, exceptions, fields
from odoo.exceptions import UserError, Warning
from datetime import datetime, date, timedelta


class ReportInvoiceCliente(models.AbstractModel):
    _name = 'report.reporte_factura_grupo_rocar.template_cliente'

    @api.model
    def _get_report_values(self, docids, data):
        if docids:
            data = {'form': self.env['account.move'].browse(docids)}
            var = data['form']
        else:
            var = self.env['account.move'].search([('id', '=', data['id'])])

        res = dict()
        docs = []
        info = []
        monto_base_exento = 0
        if var.date:
            fecha = var.date
        else:
            fecha = var.date_invoice
        fecha = datetime.strptime(str(fecha), '%Y-%m-%d')
        fecha = fecha.strftime('%d/%m/%Y')
        if var.type == 'out_invoice' or 'out_refund':
            n_factura = var.name
        elif var.type == 'in_invoice' or 'in_refund':
            n_factura = var.supplier_invoice_number
 #       n_cliente = var.partner_id.num_cliente
        razon = var.partner_id.name
        rif = var.partner_id.vat
        direccion = var.partner_id.street
        telefono = var.partner_id.phone
     #   forma_pago = var.pago_transfe.name
       # banco = var.tipo_banco.name
        cont = 0
        total = 0
        if var.invoice_origin:
            origen = 'REC'
        else:
            origen = 'FAC'
        nota_cred = var.name
        origin_number = var.name
        info.append({
            'fecha':fecha,
            'n_factura': n_factura,
            'nro_ctrl': var.nro_ctrl if var.nro_ctrl else ' ',
            'razon': razon,
            'rif': rif,
            'direccion': direccion,
            'telefono': telefono,
         #   'forma_pago': forma_pago,
          #  'banco': banco
        })
        base = 0
        for lin in var.invoice_line_ids:
            monto_base_exento = 0
            monto_base = 0
            cont += 1

            monto_base = lin.price_total - lin.price_subtotal
            base += lin.price_total - lin.price_subtotal
            if monto_base == 0:
                monto_base_exento = lin.price_subtotal
            else:
                monto_base_exento = 0

            docs.append({
                'n': cont,
                'cod': lin.product_id.default_code,
                'cant': lin.quantity,
                'um': lin.product_uom_id.name,
                'descripcion': lin.name,
            #    'lote': numero_lote,
                'precio_unitario': self.formato_cifras(lin.price_unit),
                'precio_total': self.formato_cifras(lin.price_subtotal),
            })
            total += lin.price_subtotal

        if docs:
            docs.append({
                'n': ' ',
                'cod': ' ',
                'cant': ' ',
                'um': ' ',
                'descripcion': ' ',
          #      'lote': ' ',
                'precio_unitario': ' ',
                'precio_total': ' ',
            })
        if var.env.company and var.env.company.street :
            street = str(var.env.company.street) +','
        else:
            street = ' '
        if var.env.company and var.env.company.zip:
            zip_code = str(var.env.company.zip) + ','
        else:
            zip_code = ' '
        if var.env.company and var.env.company.city:
            city = str(var.env.company.city) + ','
        else:
            city = ' '
        return {
            'data': var,
            'model': self.env['report.reporte_factura_grupo_rocar.template_cliente'],
            'lines': res,  # self.get_lines(data.get('form')),
            # date.partner_id
            'docs': docs,
            'infos': info,
            'total': self.formato_cifras(total),
            'total_total': self.formato_cifras(var.amount_total),
            'monto_iva': self.formato_cifras(var.amount_tax),
            'base': self.formato_cifras(base),
            'monto_base_exento': self.formato_cifras(monto_base_exento),
            'cifra_total': self.numero_to_letras(var.amount_total),
            'company': var.env.company,
            'street' : street,
            'zip_code': zip_code,
            'city': city,
            'origin_check': origen,
            'nota_cred': nota_cred,
            'origin_number': origin_number,

        }

    def formato_cifras(self, valor):
        monto = '{0:,.2f}'.format(valor).replace('.', '-')
        monto = monto.replace(',', '.')
        monto = monto.replace('-', ',')
        return monto

    def numero_to_letras(self,numero):
        indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
        entero = int(numero)
        decimal = int(round((numero - entero) * 100))
        # print 'decimal : ',decimal
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

        # Validad las centenas
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