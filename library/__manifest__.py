{
    'name': 'Une librairie',
    'version': '18.0.1.4',
    'summary': 'Un exemple de librairie',
    'description': "Une librairie",
    'author': 'Re-uz distribution',
    'category': 'library',
    'depends': ['base', 'web'],
    'data': [
        "views/library_view.xml",
        "views/library_category_view.xml",
        "views/library_menu.xml",
        "data/category_demo.xml",
        "data/library_security.xml",
        "security/ir.model.access.csv",
        "report/library_book_templates.xml",
        "report/library_book_report.xml"
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}