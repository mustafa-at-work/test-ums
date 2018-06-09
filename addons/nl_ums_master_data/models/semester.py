from odoo import models, fields, api


class Semister(models.Model):

    _name = 'ums.semester'
    _description = 'Semesters of a bachelor or masters degreee'

    year_id = fields.Many2one('ums.year', string="Year")

    name = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], string="Name")
    semester_type = fields.Selection([('spring', 'Spring'), ('fall', 'Fall')], string='Type')