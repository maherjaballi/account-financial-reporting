# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_export_csv = fields.Boolean(string='account export csv',
        help='Add a wizard that allow you to export a csv file based on accounting \n'
              'journal entries \n'
              '- Trial Balance \n'
              '- Analytic Balance (with accounts) \n'
              '- Journal Entries \n'
              'You can filter by date range \n'
             '-This installs the module account_export_csv.')
    
    module_account_financial_report = fields.Boolean(string='account financial report',
        help='This module adds a set of financial reports. They are accessible under \n'
              'Accounting / Reporting / OCA Reports. \n'
              '- General ledger \n'
              '- Trial Balance \n'
              '- Open Items \n'
              '- Aged Partner Balance \n'
              '- VAT Report \n'
              '- Journal Ledger \n'
              'Currently General ledger, Trial Balance and Open Items are fully compatible with a foreign \n'
              'currency set up in account in order to display balances. Moreover, any foreign \n'
              'currency used in account move lines is properly shown. \n'
              'In case that in an account has not been configured a second currency foreign \n'
              'currency balances are not available. \n')

    module_account_tax_balance = fields.Boolean(string='account tax balance',
        help='This module allows to compute tax balances within a certain date range. \n'
              'It depends on date_range module and exposes compute methods that can be called by other modules \n'
              '(like localization ones). \n')
    
    module_mis_builder_cash_flow = fields.Boolean(string='mis builder cash-flow',
        help='This module allows you to have a cash flow forecast. \n'
              'The forecast is based on two types of date: \n'
              '* Accounting entries: Due date field instead of Date \n'
              '* Forecast lines: manual lines created that forecast in/out cashflow moves. \n')

    module_partner_statement = fields.Boolean(string='partner statement',
        help='This module extends the functionality of Invoicing to support the printing of customer and vendor statements.  \n'
            'There are two types of statements, Activity and Outstanding.  Aging details can be shown in the reports, expressed in aging buckets, \n'
            'so the customer or vendor can review how much is open, due or overdue. \n'

            'The activity statement provides details of all activity on the partner receivables or payables \n'
            'between two selected dates. This includes all invoices, refunds and payments. \n'
            'Any outstanding balance dated prior to the chosen statement period will appear \n'
            'as a forward balance at the top of the statement. The list is displayed in chronological \n'
            'order and is split by currencies. \n'

            'the outstanding statement provides details of all outstanding partner receivables or payables \n'
            'up to a particular date. This includes all unpaid invoices, unclaimed refunds and \n'
            'outstanding payments. The list is displayed in chronological order and is split by currencies. \n'
             '-This installs the module partner_statement.')


   