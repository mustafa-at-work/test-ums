# -*- coding: utf-8 -*-
# 1 : imports of python lib
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
# 3 : imports from odoo modules
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Teacher(models.Model):
    # Private attributes
    _inherit = 'hr.employee'
    _description = 'Lecturers in a university'

    # Fields declaration
    age = fields.Char('Age')

    # Boolean field to check if the employee is a lecturer
    lecturer = fields.Boolean(string='Lecturer', default=False)

    # Selection fields
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
    class_ids = fields.One2many('ums.classes', 'teacher_id', string='Classes')

    # Compute field
    class_count = fields.Integer(
        string='Total classes of a lecturer',
        compute='_get_total_class')

    # Compute field to count total classes for a teacher
    @ api.one
    def _get_total_class(self):
        class_count = self.env['ums.classes'].search_count(
            [['teacher_id.id', '=', self.id]])
        self.class_count = class_count

    # Method onchange to assign the year based on birth date.
    @api.onchange('birthday')
    def set_age(self):
        for rec in self:
            if rec.birthday:
                dt = rec.birthday
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years)

    # Constraint to check age of the teacher
    @api.constrains('age')
    def _validate_age(self):
        for person in self:
            if int(person.age) < 25:
                raise ValidationError(
                    'The age of a lecturer can not be less 25 !')
            if int(person.age) > 65:
                raise ValidationError(
                    'The age fo a lecturer can not be greater than 65 !')
