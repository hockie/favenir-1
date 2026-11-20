from odoo import fields, models

class StudentStudent(models.Model):
    _name = "student.student"
    _description = "Student Module"
    
    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    
    description = fields.Text()
    gender = fields.Selection(string="Level",
                              selection=[
                                 ('male','Male'),
                                 ('female','Female'),
                                 ('other','Other'),
                             ],
                             copy=False)
    email = fields.Char(string="Email", widget="email")
    phone = fields.Char(string="Phone", widget="phone")
    address = fields.Text(string="Address")
    city = fields.Char(string="City")