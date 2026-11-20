
from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Management'
    _rec_name = 'name'
    _order = 'name asc'

    # Basic Information
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

    # Address Information
    address = fields.Char(
        string='Address'
    )

    city = fields.Char(
        string='City'
    )

    # Additional Information
    description = fields.Text(
        string='Description'
    )

    # Record Status
    active = fields.Boolean(
        string='Active',
        default=True
    )
