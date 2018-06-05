# -*- coding: utf-8 -*-


# 1 : imports of python lib
# 2 : imports of odoo
from odoo import api, fields, models  # alphabetically ordered
# 3 : imports from odoo modules


class Lecture(models.Model):
    # Private attributes
    _name = 'nl_ums.lecture'
    _description = 'Lectures to be thought in a class for a course'
    _order = 'date asc'
    _rec_name = 'title'

    # Fields declaration
    title = fields.Many2many('master.topic', string='Title')
    date = fields.Date('Date', required=True)
