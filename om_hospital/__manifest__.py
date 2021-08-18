# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """Hospital Managemet System """,
    'author': "AlaaAkiel",
    'website': "http://alaaprog.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'web'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/doctor.xml',
        'views/majors.xml',
        'views/booking.xml',
        'views/patient.xml',
        'views/dashborad.xml',
        # 'views/template/appointment.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/template/custom_login.xml',
    ],
    'qweb': [
        "static/src/xml/menu.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
