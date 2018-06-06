# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Material(models.Model):
    # Private attributes
    _name = 'ums.material'
    _description = 'Materials for lectures and classes'

    # Fields declaration
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    type = fields.Char('Type', required=True)
    source_file = fields.Binary('Material File')

    # SQl constraints to check uniqueness of material names
    _sql_constraints = [
        ('material_name_unique',
         'UNIQUE(name)',
         'Materials name should be unique!')]

    # Relational fields
    lecture_ids = fields.Many2many('ums.lecture', string='Lectures')
    class_ids = fields.Many2many('ums.classes', string='Classes')
