# -*- coding: utf-8 -*-
{
    'name': "My pet - minhng.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security\ir.model.access.csv',
        'views\my_pet_views.xml',
        r'wizard\batch_update.xml',
        r'views\template.xml',
        r'views\res_config_settings_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}