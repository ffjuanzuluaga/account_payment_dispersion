# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Account Payment Dispersal',
    'version': '0.1',
    'category': 'Localization/Accounting & Finance',
    'description': 'This module allows to visualise the different dispersions that have been carried out over time..',
    'author': 'Firefly Software Consulting S.A.S',
    'maintainer': 'Firefly Software Consulting S.A.S',
    'website': 'https://firefly-e.com/',
    'depends': [
        'account',
        'l10n_co'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_bank_data.xml',
        'views/account_payment_views.xml',
        'views/res_bank_views.xml',
        'views/account_payment_dispersal_views.xml',
        'views/res_partner_bank_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml'
    ],
    'license': 'OPL-1',
    'application': False,
    'installable': True,
    'currency': 'USD',
    'price': 20.00,

}
