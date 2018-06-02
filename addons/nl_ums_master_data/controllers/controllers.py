# -*- coding: utf-8 -*-
from odoo import http

# class NlUmsMasterData(http.Controller):
#     @http.route('/nl_ums_master_data/nl_ums_master_data/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nl_ums_master_data/nl_ums_master_data/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nl_ums_master_data.listing', {
#             'root': '/nl_ums_master_data/nl_ums_master_data',
#             'objects': http.request.env['nl_ums_master_data.nl_ums_master_data'].search([]),
#         })

#     @http.route('/nl_ums_master_data/nl_ums_master_data/objects/<model("nl_ums_master_data.nl_ums_master_data"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nl_ums_master_data.object', {
#             'object': obj
#         })