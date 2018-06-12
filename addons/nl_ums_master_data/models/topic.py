# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Topic(models.Model):
    _name = 'ums.topic'
    _description = 'Course Topics'

    # Fields declaration
    title = fields.Char(string='Title')
    description = fields.Text()

    # Relational fields
    course_id = fields.Many2one('ums.course')
    lecture_ids = fields.Many2many('ums.lecture', 'ums_lecture_ums_topic_rel', string='Lectures')

    # SQL Constraint to check uniqueness of topic names
    _sql_constraints = [
            ('topic_title_unique',
             'UNIQUE(title)',
             'Title of lectures must be unique!')]