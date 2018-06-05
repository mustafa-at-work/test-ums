# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Classes(models.Model):
    _name = 'ums.classes'
 
    # department_id=fields.Many2one('ums.department', string='Department', required=True)
    # faculty_id=fields.Many2one('ums.faculty', string='Faculty', required=True)
    # section_ids=fields.One2many('ums.sections','class_id', string='Sections')

    name = fields.Char('Class Name', required=True)
    department_id=fields.Many2one('ums.department', string='Department', required=True)
    semester_id = fields.Many2one('ums.semister', string='Semester', required=True)
    course_id = fields.Many2one('ums.course', string='Course', required=True)
    lecturer_id = fields.Many2one('res.partner', string='Lecturer', required=True)
    education_year = fields.Many2one('ums.year',required=True, string='Education Year')
    timing=fields.Many2one('ums.timing', string='Timing', required=True)
    start_time = fields.Char('Start time')
    end_time = fields.Char('End time')
    class_room=fields.Many2one('ums.class_room', string='Class room', required=True)
    
    year = fields.Selection([
        ('firstYear','First Year'),
        ('secondYear','Second Year'),
        ('thirdYear','Third Year'),
        ('fourthYear','Fourth Year'),
    ], default='firstYear')

    student_ids=fields.Many2many('ums.students', string='Studetns')