# -*- coding: utf-8 -*-
from openerp import http

# class FormaPago(http.Controller):
#     @http.route('/forma_pago/forma_pago/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/forma_pago/forma_pago/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('forma_pago.listing', {
#             'root': '/forma_pago/forma_pago',
#             'objects': http.request.env['forma_pago.forma_pago'].search([]),
#         })

#     @http.route('/forma_pago/forma_pago/objects/<model("forma_pago.forma_pago"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('forma_pago.object', {
#             'object': obj
#         })