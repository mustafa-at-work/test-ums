from odoo import fields, models, api


class Building(models.Model):
    _name = 'ums.building'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=True)
    location = fields.Char('Location', required=True)

    # Relational fields
    class_room_ids = fields.One2many('ums.class_room', 'floor_id', string='Class rooms')
    floor_ids = fields.One2many('ums.floor', 'building_id', string='Floor')