# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Mail Inherit',
    'version' : '1.1',
    'summary': 'Odoo Training',
    'sequence': 30,
    'description': """
Odoo Training
====================
Odoo Training
    """,
    'category': 'Odoo Training',
    'website': 'https://www.odoo.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['mail', 'sale'],
    'data': [
        'views/mass_mailing_views.xml',
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
