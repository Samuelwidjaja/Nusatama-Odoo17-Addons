# extend_account_invoice/__manifest__.py
{
    'name': 'Extend Account Invoice',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Adds sbu_jurnal dropdown to account.move',
    'author': 'handaru',
    'depends': ['account', 'sale'],
    'data': [
        'report/report_extend_invoice_customerpo.xml',
	'report/report_extend_invoice.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
}
