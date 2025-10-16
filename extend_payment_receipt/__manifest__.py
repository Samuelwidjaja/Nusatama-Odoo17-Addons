{
    'name': 'Extend Payment Receipt',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Add SBU field to payment form and receipt report',
    'depends': ['account'],
    'data': [
        'views/account_payment_views.xml',
        'report/account_payment_report.xml',
	'report/account_payment_format.xml',
    ],
    'installable': True,
    'application': False,
}
