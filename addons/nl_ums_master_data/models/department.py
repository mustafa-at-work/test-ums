from odoo import models, fields, api


class Department(models.Model):
    _name = 'ums.department'
    _description = 'Department'

    faculty_id = fields.Many2one('ums.faculty', string='Faculty Name')
    course_ids = fields.Many2many('ums.course', string='Courses')

    name = fields.Char('Department Name', required=True)

    teacher_ids = fields.One2many('ums.teacher',  string='Department')