from odoo import models, fields, api


class Course(models.Model):
<<<<<<< HEAD
=======

>>>>>>> aaf2ec12e747fed299cf82c5530dc9d217c37849
    _name = 'ums.course'
    _description = 'Course'
    _rec_name = "title"

    title = fields.Char('Title', required=True)
<<<<<<< HEAD
    description = fields.Text('Description')
=======
    description = fields.Text('Description')
>>>>>>> aaf2ec12e747fed299cf82c5530dc9d217c37849
