# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sections(models.Model):
    _name = 'ums.sections'

    name = fields.Char('Secsion Name', required=True)
    class_id = fields.Many2one('ums.classes', string='Class', required=True)
    department_id=fields.Many2one('ums.department', string='Department', ewquired=True)
    semester_id = fields.Many2one('ums.semister', string='Department', required=True)
    course_id = fields.Many2one('ums.course', string='Semester', required=True)
    lecturer_id = fields.Many2one('res.partner', string='Lecturer', required=True)
    year = fields.Many2one('ums.year',required=True)
    timing=fields.Many2one('ums.timing', string='Timing', required=True)
    start_time = fields.Char('Start time')
    end_time = fields.Char('End time')
    class_room=fields.Many2one('ums.class_room', string='Class room', required=True)

     
