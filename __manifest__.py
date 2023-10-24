# -*- coding: utf-8 -*-
{
    'name': 'County HR',

    'summary': """
        Capture details of the Human Resource wealth in a region
        """,

    'description': """
Human Resources Management.
============================

Capture the 
* Territorial locations (subcounties and villages).
* HR personal details
* HR academic qualifications

#ToDo portal access for personal profiles

    """,
    'author': "Cyrus G. Waithaka",
    'website': "http://www.exploredatasystems.com",
    "version": "16.0.1.1.0",
    "category": "Human Resources",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'views/base_views.xml',
        'views/human_resource_views.xml',
        'views/location_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
