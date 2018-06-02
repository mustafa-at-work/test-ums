from odoo import models, fields, api

class Course(models.Model):
	
    _name = 'ums.course'
    _description = 'Course'
    _rec_name="title"

    title = fields.Char('Title', required=True)
    description = fields.Text('Description')
    
  