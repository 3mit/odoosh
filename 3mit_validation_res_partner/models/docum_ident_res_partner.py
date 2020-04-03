# -*- coding: UTF-8 -*-
#    type of the change:  Created
#    Comments: Creacion de generacion de codigo para clientes y proveedores (depends for res_partner)



from odoo import fields, models, api,exceptions


class ValidationDocument(models.Model):
    _inherit = 'res.partner'

    NACIONALIDAD = [
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'Pasaporte')]
    nationality = fields.Selection(NACIONALIDAD, string="Tipo Documento")
    identification_id = fields.Char('Documento de Identidad', size=20)


    def validation_document_ident(self, valor):
    #    if valor.isdigit() == False:
    #        raise exceptions.except_orm(('Advertencia!'), (u'La Cédula solo debe contener números'))
        if (len(valor) > 20) or (len(valor) < 7):
            raise exceptions.except_orm(('Advertencia!'),
                                        (u'El Documento no puede ser menor que 7 cifras ni mayor a 20.'))
        return


    def validate_ci_duplicate(self, valor, create=False):
        found = True
        partner_2 = self.search([('identification_id', '=', valor)])
        for cus_supp in partner_2:
            if create:
                if cus_supp and (cus_supp.customer_rank or cus_supp.supplier_rank):
                    found = False
                elif cus_supp and (cus_supp.customer_rank or cus_supp.supplier_rank):
                    found = False
        return found


    def write(self, vals):
        res = {}
        if vals.get('identification_id'):
            valor = vals.get('identification_id')
            self.validation_document_ident(valor)
        if not self.validate_ci_duplicate(vals.get('identification_id', False)):
            raise exceptions.except_orm(('Advertencia!'),
                                        (u'El cliente o proveedor ya se encuentra registrado con el Documento: %s') % (
                                            vals.get('identification_id', False)))
        res = super(ValidationDocument, self).write(vals)
        return res

    @api.model
    def create(self, vals):
        res = {}
        if vals.get('identification_id'):
            valor = vals.get('identification_id')
            self.validation_document_ident(valor)
        if vals.get('identification_id'):
            if not self.validate_ci_duplicate(vals.get('identification_id', False), True):
                raise exceptions.except_orm(('Advertencia!'),
                                            (u'El cliente o proveedor ya se encuentra registrado con el Documento: %s') % (
                                                vals.get('identification_id', False)))
        res = super(ValidationDocument, self).create(vals)
        return res
