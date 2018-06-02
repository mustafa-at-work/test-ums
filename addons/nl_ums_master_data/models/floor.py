from odoo import fields, models, api

class Floor(models.Model):
    _name='ums.floor'

    name=fields.Char('Name', required=True)
    building_id=fields.Many2one('ums.building', string='Building', required=True)