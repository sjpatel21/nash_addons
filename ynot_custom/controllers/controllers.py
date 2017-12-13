# -*- coding: utf-8 -*-
from odoo import http

# class ../customAddonsDir/nashAddons/(http.Controller):
#     @http.route('/../custom_addons_dir/nash_addons//../custom_addons_dir/nash_addons//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../custom_addons_dir/nash_addons//../custom_addons_dir/nash_addons//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../custom_addons_dir/nash_addons/.listing', {
#             'root': '/../custom_addons_dir/nash_addons//../custom_addons_dir/nash_addons/',
#             'objects': http.request.env['../custom_addons_dir/nash_addons/.../custom_addons_dir/nash_addons/'].search([]),
#         })

#     @http.route('/../custom_addons_dir/nash_addons//../custom_addons_dir/nash_addons//objects/<model("../custom_addons_dir/nash_addons/.../custom_addons_dir/nash_addons/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../custom_addons_dir/nash_addons/.object', {
#             'object': obj
#         })