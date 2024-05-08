{
    'name': 'CompanyConnect',
    'version': '1.0',
    'category': 'Human Resources/CompanyConnect',
    'summary': 'Connect between employees',
    'description': """
        This module aims to manage employee's attendances.
    """,
    'depends': ['hr'],
    'data': [
        'views/hr_attendance_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}