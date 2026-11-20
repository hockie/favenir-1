
{
    'name': 'Student Module',
    'version': '19.0.1.0.0',
    'category': 'Custom Modules/Tech Training',
    'summary': 'Module to handle Student Records',

    'description': """
        Module to handle:
        - Students
        - Exams
        - Grades
    """,

    'license': 'OPL-1',
    'author': 'Hockie',
    'website': 'https://www.favenir.com',

    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        # Security
        'security/student_groups.xml',
        'security/student_security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/student_views.xml',
        'views/student_menuitems.xml',
    ],

    'application': True,
    'installable': True,

    'web_icon': 'students,static/description/icon.png',
}
