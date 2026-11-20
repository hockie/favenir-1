{
    'name': 'Student Module',
    'version': '19.0.1.0.0',
    'category': 'Academe',
    'summary': """Module to handle Student Records""",
    'description': """Module to handle:
        - Students
        - Exams
        - Grades
        """,
    'license': 'OPL-1',
    'author': 'Hockie',
    'website': 'www.favenir.com',
    'category': 'Custom Modules/Tech Training',
    'version': '1.0',
    'depends': ['base','contacts'],
    'data': [
        'security/student_groups.xml',
        'security/student_security.xml',
        'views/student_views.xml',
        'views/student_menuitems'
            ],
    'installable': True,
    'application': True,
    'web_icon': 'students,static/description/icon.png',
    
    
}