# -*- coding: utf-8 -*-
from odoo import http


class AngularWebsite(http.Controller):
    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/angular_website/angular_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('angular_website.listing', {
#             'root': '/angular_website/angular_website',
#             'objects': http.request.env['angular_website.angular_website'].search([]),
#         })

#     @http.route('/angular_website/angular_website/objects/<model("angular_website.angular_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('angular_website.object', {
#             'object': obj
#         })
