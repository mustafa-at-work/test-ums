from odoo import fields, models, api


class Timing(models.Model):
    _name = 'ums.timing'
    _rec_name = 'batch_time'

    batch_time = fields.Char('Name', required=True)
