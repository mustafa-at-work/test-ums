from odoo import models, fields, api

class Faculty(models.Model):
	
    _name = 'ums.faculty'
    _description = 'Faculty'

    department_ids = fields.One2many('ums.department', 'faculty_id', string='Departments')

    name = fields.Char('Faculty Name', required=True)
  
    
  