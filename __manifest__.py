# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'quan ly sinh vien',
    'version': '1.2',
    'summary': 'qlsv',
    'sequence': 1,
    'description': """
        Demo 
    """,
    'category': '',
    'depends': ['sale'],
    'data': [
            'security/ir.model.access.csv',
            'views/department_view.xml',
            'views/course_view.xml',
            'views/class_view.xml',
            'views/subject_view.xml',
            'views/point_view.xml',
            'wizard/wizard_student_view.xml',
            'views/student_view.xml',
            'views/menu_view.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
