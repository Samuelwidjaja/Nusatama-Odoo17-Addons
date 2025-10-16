{
    'name': 'Extend Sale Order PPD',
    'version': '1.0',
    'depends': ['sale', 'base'],
    'category': 'Sales',
    'author': 'handy',
    'summary': 'Customizations to Sale Order and Quotation Report',
    'data': [
        'views/sale_order_view.xml',
        'report/sale_order_report.xml', 
    ],
    'installable': True,
    'auto_install': False,
}
