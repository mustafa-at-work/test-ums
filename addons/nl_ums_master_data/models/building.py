from odoo import fields, models, api

class Building(models.Model):
    _name='ums.building'

    name=fields.Char('Name', required=True)
    description=fields.Text('Description', required=True)
    location=fields.Char('Location', required=True)
    