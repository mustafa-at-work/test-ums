# -*- coding: utf-8 -*-


# 1 : imports of python lib
# 2 : imports of odoo
from odoo import api, fields, models  # alphabetically ordered
# 3 : imports from odoo modules


class Lecture(models.Model):
    # Private attributes
    _name = 'ums.lecture'
    _description = 'Lectures to be thought in a class for a course'
    _order = 'date asc'
    # _rec_name = 'title_ids'

    # Fields
    description = fields.Text('Description')
    date = fields.Date('Date', required=True)
    state = fields.Selection([
        ('not held', 'Not Held'),
        ('ongoing', 'Ongoing'),
        ('held', 'Held')])

    color = fields.Integer()

    # Related field
    title = fields.Char(related='title_ids.title')

    # Relational fields
    title_ids = fields.Many2many('ums.topic', 'ums_lecture_ums_topic_rel', string='Title', required=True)
    material_ids = fields.Many2many('ums.material', string='Materials')

