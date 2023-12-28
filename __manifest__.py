# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Account Payment Dispersal',
    'version': '0.1',
    'category': 'Localization/Accounting & Finance',
    'description': 'This module allows to visualise the different dispersions that have been carried out over time..',
    'author': 'Firefly-e',
    'maintainer': 'Firefly-e',
    'website': 'https://firefly-e.com/',
    'depends': [
        'l10n_co'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res.bank.csv',

        'views/res_bank_views.xml',
        'views/account_payment_dispersal_views.xml',
        'views/res_partner_bank_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml'
    ],
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
}
