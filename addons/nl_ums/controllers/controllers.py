# -*- coding: utf-8 -*-
from odoo import http

# class NlUms(http.Controller):
#     @http.route('/nl_ums/nl_ums/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nl_ums/nl_ums/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nl_ums.listing', {
#             'root': '/nl_ums/nl_ums',
#             'objects': http.request.env['nl_ums.nl_ums'].search([]),
#         })

#     @http.route('/nl_ums/nl_ums/objects/<model("nl_ums.nl_ums"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nl_ums.object', {
#             'object': obj
#         })
