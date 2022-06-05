# -*- coding: utf-8 -*-
# from odoo import http


# class Licoreria(http.Controller):
#     @http.route('/licoreria/licoreria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/licoreria/licoreria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('licoreria.listing', {
#             'root': '/licoreria/licoreria',
#             'objects': http.request.env['licoreria.licoreria'].search([]),
#         })

#     @http.route('/licoreria/licoreria/objects/<model("licoreria.licoreria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('licoreria.object', {
#             'object': obj
#         })
