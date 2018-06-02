from odoo import fields, models, api

class ClassRoom(models.Model):
    _name='ums.class_room'

    name=fields.Char('Name', required=True)
    building_id=fields.Many2one('ums.building', string='Building')
    floor_id=fields.Many2one('ums.floor', string='Floor')