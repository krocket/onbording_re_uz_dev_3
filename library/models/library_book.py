from odoo import fields, models, UserError
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Book(models.Model):
  _name = 'library.book'
  _description = 'Book'
  name = fields.Char(string='Title', required=True)
  isbn = fields.Char('ISBN')
  active = fields.Boolean(string='Active?', default=True)
  date_publisher = fields.Date()
  image = fields.Binary('Cover')
  publisher_id = fields.Many2one('res.partner', string='Publisher')
  author_ids = fields.Many2many('res.partner', string='Authors')
  category_ids = fields.Many2many('library.book.category', string='Categories')

  def _check_isbn(self):
    self.ensure_one()
    digits = [int(x) for x in self.isbn if x.isdigit()]
    if len(digits) == 13:
      return True
    else : 
      return False

  def button_check_isbn(self):
    _logger.info(self)
    for book in self:
      if not book.isbn:
        raise UserError(
          'Please provide an ISBN13 for %s' % book.name)
      if book.isbn and not book._check_isbn():
        raise UserError(
          '%s is an invalid ISBN' % book.isbn)
      return True
    
  def button_your_are_best(self):
    raise UserError("T'es le meilleurs")
