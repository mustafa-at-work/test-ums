# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Topic(models.Model):
    _name = 'master.topic'
    _description = 'Course Topic'
    _rec_name = 'title'

    title = fields.Char(string='Title')
    description = fields.Text()

    # sql constraint to check uniqueness of topic title
    _sql_constraints = [
        ('topic_title_unique',
         'UNIQUE(title)',
         'Title of lectures must be unique!')]
