from odoo import models, fields, api


class Department(models.Model):

    _name = 'ums.department'
    _description = 'Department'

    faculty_id = fields.Many2one('ums.faculty', string='Faculty Name')
    course_ids = fields.Many2many('ums.course', string='Courses')
    lecturer_ids = fields.One2many('hr.employee', string='Lecturers')

    name = fields.Char('Department Name', required=True)
