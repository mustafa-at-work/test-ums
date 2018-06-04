        ('married', 'Married'),
        ('divorce', 'Divorced'),
        ('widowed','Widowed')
        
        ],string="Status")

    dob=fields.Date(string="DOB",required=True)
    age=fields.Char('Age')
    
    color=fields.Integer()
    
   
    # color=fields.Integer()

    # when click the checkbox current address is set to permanent address

    # On change api
    @api.onchange('same_as_current_address')
    def _set_permanent_address(self):
        if self.same_as_current_address == True:
            self.permanent_province = self.current_province
            self.permanent_district = self.current_district
            self.permanent_village = self.current_village
        elif self.same_as_current_address == False:
            self.permanent_province = " "
            self.permanent_district = " "
            self.permanent_village = " "
            

    @api.onchange('dob')
    def set_age(self):
            if rec.dob:
                dt = rec.dob
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = int(rd.years)


    @api.depends('addmission_date')
    def _get_current_date(self):
        for record in self:
            record.addmission_date = date.today()


    @api.constrains('age')
    def _check_age(self):
        if self.age < 18:
            raise ValidationError(_('You are not enough older: %s' % self.age))
        elif self.age > 50:
            raise ValidationError(_('You are too older: %s' % self.age))


    _sql_constraints = [
        ('tazkira_no_uniq', 'unique (tazkira_no)', 'This Tazkira number is already exists!')
    ]
