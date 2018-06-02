# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Class(models.Model):
    _name = 'nl_ums.class'

    name = fields.Char('Class Name')