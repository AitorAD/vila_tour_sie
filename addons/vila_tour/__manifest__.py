# -*- coding: utf-8 -*-
{
    'name': "VilaTour",

    'summary': """
        Aplicación turística para Villajoyosa""",

    'description': """
        Una app desarrollada con el objetivo de fomentar el turismo local en La Vila Joiosa
    """,

    'author': "Team AJO",
    'website': "https://www.teamAjo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tourism',
    'version': '0.4',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/views.xml',
        'views/views_ingredient.xml',
        'views/views_recipes.xml',
        'views/views_reviews.xml',
        'views/views_categories.xml',
        'views/views_places.xml',
        'views/views_festivals.xml',
        'views/views_users.xml',
        'report/report_recipes.xml',
        'report/report_festivals.xml',
        'report/report_places.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'vila_tour/static/src/css/style.css',  # Asegúrate de usar la ruta correcta
        ],
    },
}
