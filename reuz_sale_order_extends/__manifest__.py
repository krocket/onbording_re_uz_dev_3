{
    'name': 'Surcharge du module vente',
    'version': '18.0.1.0',
    'summary': 'Un exemple de Surcharge du module de ventes',
    'description': "Surcharge du module vente",
    'author': 'Re-uz distribution',
    'category': 'sales',
    'depends': ['sale_management'],
    'data': [
        "views/sale_order_extends_view.xml",
        "report/sale_order_extends_template.xml"
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}