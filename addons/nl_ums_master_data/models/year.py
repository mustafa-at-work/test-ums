from odoo import fields, models, api


class Year(models.Model):
    _name = 'ums.year'

    _rec_name = 'year'

    year = fields.Char('Year', required=True)
    sequence = fields.Integer('Sequence', required=True)
    first_day_of_year = fields.Date('First Day Of Year', required=True)
    last_day_of_year = fields.Date('Last Day Of Year', required=True)
