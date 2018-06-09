# -*- coding: utf-8 -*-
{
    'name': "nl_ums_master_data",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/master_views.xml',
        'views/topic_views.xml',
        'views/course_views.xml',
        'views/faculty_views.xml',
        'views/department_views.xml',
        'views/timing_views.xml',
        'views/class_room_views.xml',
        'views/floor_views.xml',
        'views/building_views.xml',
        'views/semester_views.xml',
        'views/year_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}