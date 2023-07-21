# -*- coding: utf-8 -*-
{
    'name': "School",
    'summary': """School management model""",
    'description': """Managing school information""",
    'author': "Lam Quoc Phu",
    'website': "https://quocphu.info",
    'category': 'Uncategorized',
    'version': '1.1',
    'depends': [],
    'data': [
        'security\ir.model.access.csv',
        'views\school_info.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}