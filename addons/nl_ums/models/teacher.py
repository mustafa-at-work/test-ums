# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Teacher(models.Model):
    # Private attributes
    _name = 'ums.teacher'
    _description = 'Lecturers in university'

    # Fields declaration
    name = fields.Char(required=True)
    phone_number = fields.Char(string='Phone number')
    address_id = fields.Char('Address')
    email_address = fields.Char('Email address')
    id_number = fields.Integer('ID number')
    citizenship = fields.Char('Citizenship')

    # Selection fields
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')])
    age = fields.Integer('Age')
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

    # sql constraint to check uniqueness of id_number
    _sql_constraints = [
        (
            'Unique ID number',
            'UNIQUE(id_number)',
            'The ID number should be unique!')]