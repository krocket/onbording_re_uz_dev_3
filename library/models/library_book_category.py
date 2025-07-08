from odoo import fields, models

class BookCategory(models.Model):
  _name = 'library.book.category'
  _description = 'Book Category'

  name = fields.Char(translate=True, required=True)

  parent_id = fields.Many2one(
    comodel_name='library.book.category',
    string='Parent Category',
    ondelete='restrict'
  )

  child_ids = fields.One2many(
    comodel_name='library.book.category',
    inverse_name='parent_id',
    string='Subcategories'
  )