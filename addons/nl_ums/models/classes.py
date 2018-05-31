# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UMSClasses(models.Model):
    _name='ums.classes'

    name=fields.Char('Class Name')