from odoo import fields, models
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ReuzSalesOrder(models.Model):
  _inherit = 'sale.order'

  silver_reference = fields.Char(string='Silver reference', required=True)
  planned_date = fields.Date(string='Date de plannification')

  def send_alerte_test():
    raise UserError('T\'es le meilleur')