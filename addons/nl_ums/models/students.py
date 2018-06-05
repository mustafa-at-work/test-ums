from odoo import models, fields, api


class Student(models.Model):
    _name = 'ums.students'
    _rec_name = 'fullname'

    description = 'Student Model'

    fullname = fields.Char(string='Full Name', required=True)
    fatherName = fields.Char(string='Father Name', required=True)
    phone = fields.Char('Phone')
    email = fields.Char(string='Email', required=True)

    tazkira_no = fields.Integer(string='National ID', required=True)
    passport_no = fields.Char(string="Passport No")
    nationality = fields.Char('Nationality')
    country = fields.Char('Country')

    current_province = fields.Char('Province', required=True)
    current_district = fields.Char('District', required=True)
    current_village = fields.Char('Village', required=True)

    same_as_current_address = fields.Boolean('Set Permanent Address as Current ')

    permanent_province = fields.Char('Province', required=True)
    permanent_district = fields.Char('District', required=True)
    permanent_village = fields.Char('Village', required=True)

    school = fields.Char(string='Graduation School', required=True)

    faculty = fields.Char('Faculty')
    department = fields.Char('Department')
    rno = fields.Char('Role Number')
    addmission_date = fields.Date('Addmission Date')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", required=True)

    status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorce', 'Divorced'),
        ('widowed', 'Widowed')

    ], string="Status")

    dob = fields.Date(string="DOB", required=True)
    age = fields.Char('Age')

    # color=fields.Integer()

    # when click the checkbox current address is set to permanent address

    # On change api
    @api.onchange('same_as_current_address')
    def _set_permanent_address(self):
        if self.same_as_current_address == True:
            self.permanent_province = self.current_province
            self.permanent_district = self.current_district
            self.permanent_village = self.current_village

     