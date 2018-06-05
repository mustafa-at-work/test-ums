from odoo import models, fields, api


class Semister(models.Model):

    _name = 'ums.semister'
    _description = 'Semister'

    year_id = fields.Many2one('ums.year', string="Year")

    name = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], string="Name")
    semister_type = fields.Selection([('spring', 'Spring'), ('fall', 'Fall')], string='Type')
