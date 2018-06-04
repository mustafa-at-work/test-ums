# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Classes(models.Model):
    _name = 'ums.classes'

    name = fields.Selection([
        ('firstYear','First Year'),
        ('secondYear','Second Year'),
        ('thirdYear','Third Year'),
        ('fourthYear','Fourth Year'),
    ], default='firstYear')


    department_id=fields.Many2one('ums.department', string='Department', required=True)
    faculty_id=fields.Many2one('ums.faculty', string='Faculty', required=True)
    section_ids=fields.One2many('ums.sections','class_id', string='Sections')
     