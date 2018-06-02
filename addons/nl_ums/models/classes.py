# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Classes(models.Model):
    _name = 'ums.classes'

    name = fields.Char('Name', required=True)
    course = fields.Char('Course', required=True)
    semester = fields.Char('Semester', required=True)
    year = fields.Date('Year')
    start_date = fields.Date('Start date')
    end_date = fields.Date('End date')
