from odoo import models, fields, api


class Course(models.Model):

    _name = 'ums.course'
    _description = 'Course'
    _rec_name = "title"

    title = fields.Char('Title', required=True)
    credit = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], string="Credit")
    description = fields.Text('Description')
