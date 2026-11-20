from odoo import models, fields
class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Management'
    _rec_name = 'name'
    _order = 'name asc'
    name = fields.Char(
        string='Student Name',
        required=True
    )
    email = fields.Char(
        string='Email'
    )
    phone = fields.Char(
        string='Phone'
    )
    address = fields.Char(
        string='Address'
    )
    city = fields.Char(
        string='City'
    )

    description = fields.Text(
        string='Description'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )