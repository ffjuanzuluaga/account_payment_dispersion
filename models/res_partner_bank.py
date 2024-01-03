# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, _, exceptions

_logger = logging.getLogger(__name__)

class ResPartnerBank(models.Model):

    _inherit = 'res.partner.bank'
    
    @staticmethod
    def _get_type_of_account():
        return [
            ('no_account', _('No Account')),
            ('current_account', _('Current Account')),
            ('savings_account', _('Savings Account')),
            ('payroll_account', _('Payroll Account'))
        ]

    type_of_account = fields.Selection(selection = "_get_type_of_account", string='Type of account')