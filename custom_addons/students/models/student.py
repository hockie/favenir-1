from odoo import fields, models

class Student(models.Model):
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