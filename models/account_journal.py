# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, _, exceptions

_logger = logging.getLogger(__name__)

class AccountJournal(models.Model):

    _inherit = 'account.journal'

    @staticmethod
    def _get_type_of_account():
        return [
            ('current_account', _('Checking')),
            ('savings_account', _('Savings'))
        ]

    account_number = fields.Char(string = 'Account Number')
    account_type = fields.Selection(selection="_get_type_of_account", string = 'Account Type')