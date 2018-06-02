# -*- coding: utf-8 -*-

from odoo import models, fields, api


<<<<<<< HEAD
class Class(models.Model):
    _name = 'nl_ums.class'

    name = fields.Char('Class Name')
=======
class Classes(models.Model):
    _name = 'ums.classes'

    name = fields.Char('Name', required=True)
    course = fields.Char('Course', required=True)
    semester = fields.Char('Semester', required=True)
    year = fields.Date('Year')
    start_date = fields.Date('Start date')
    end_date = fields.Date('End date')
>>>>>>> aa5dae07ccf6198b15786205fdba78612a02054a
