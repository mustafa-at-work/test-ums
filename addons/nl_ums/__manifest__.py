# -*- coding: utf-8 -*-
{
    'name': "Test University Management System",

    'summary': """
        Test University Management System""",

    'description': """
        Test University Management System
    """,

    'author': "odoo interns",
    'website': "http://www.testcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'nl_ums_master_data'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/students_views.xml',
        'views/classes_views.xml',
        'views/students_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
