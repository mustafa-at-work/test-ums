# -*- coding: utf-8 -*-
# 1 : imports of python lib
import re
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
# 3 : imports from odoo modules
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Teacher(models.Model):
    # Private attributes
    _name = 'ums.teacher'
    _description = 'Lecturers in university'

    # Fields declaration
    name = fields.Char(required=True)
    phone_number = fields.Char(string='Phone number')
    address_id = fields.Char('Address')
    email_address = fields.Char('Email address')
    id_number = fields.Char('ID number')
    citizenship = fields.Char('Citizenship')
    birth_date = fields.Date('Birth date')
    age = fields.Char('Age')

    # Selection fields
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')])
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')])
    academic_degree = fields.Selection([
        ('pohanyar', 'Pohanyar'),
        ('Pohiyalai', 'Pohilayai'),
        ('pohandoi', 'Pohandoi'),
        ('pohand', 'Pohand')])
    educational_degree = fields.Selection([
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PHD')])

    # Relational fields
    department_id = fields.Many2one('ums.department', string='Department')
    class_ids = fields.One2many('ums.classes', 'teacher_id', string='Classes')

    # Compute field
    class_count = fields.Integer(string='Total class of a lecturer', compute='_get_total_class')

    # Compute field to count total classes for a teacher
    @ api.one
    def _get_total_class(self):
        class_count = self.env['ums.classes'].search_count([['teacher_id.id', '=', self.id]])
        self.class_count = class_count

    # sql constraint to check uniqueness of id_number
    _sql_constraints = [
        (
            'Unique ID number',
            'UNIQUE(id_number)',
            'The ID number should be unique!')]

    # Method onchange to assign the year based on birth date.
    @api.onchange('birth_date')
    def set_age(self):
        for rec in self:
            if rec.birth_date:
                dt = rec.birth_date
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years)

    # Constraint to check age of the teacher
    @api.constrains('age')
    def _validate_age(self):
        for person in self:
            if int(person.age) < 25:
                raise ValidationError('The age of a lecturer can not be less 25 !')
            if int(person.age) > 65:
                raise ValidationError('The age fo a lecturer can not be greater than 65 !')

    # Method to validate email address field
    @api.constrains('email_address')
    def _validate_email_address(self):
        for person in self:
            if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
                            person.email_address):
                raise ValidationError('Please enter a valid email address!')

