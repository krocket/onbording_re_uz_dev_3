from odoo import fields, models
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Book(models.Model):
  _inherit = 'library.book'

  is_available = fields.Boolean('Is Available ?')
  isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
  publisher_id = fields.Many2one(index=True)

  def _check_isbn(self):
    self.ensure_one()
    digits = [int(x) for x in self.isbn if x.isdigit()]
    if len(digits) == 10:
      return True
    else : 
      return super()._check_isbn()
  

