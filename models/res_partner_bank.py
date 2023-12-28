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
            ('current_account', _('Current account')),
            ('savings_account', _('Savings account')),
            ('payroll_account', _('Payroll account'))
        ]

    type_of_account = fields.Selection(selection = "_get_type_of_account", string='Type of account')