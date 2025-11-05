{
    'name': 'Extend Stock Picking Carry Customer PO',
    'version': '1.0',
    'category': 'Stock',
    'summary': 'Carry Customer PO number from SO to Delivery Order',
    'depends': ['sale_stock', 'stock', 'sale_management'], 
    'data': [
              'views/stock_picking_view.xml',
              ],
    'installable': True,
    'application': False,
}
