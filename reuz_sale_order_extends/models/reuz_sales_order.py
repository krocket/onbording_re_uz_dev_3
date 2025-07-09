from odoo import fields, models, api
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ReuzSalesOrder(models.Model):
  _inherit = 'sale.order'

  silver_reference = fields.Char(string='Silver reference')
  planned_date = fields.Date(string='Date de plannification')
  format_product = fields.Char(string='Format')
  volume_product = fields.Integer(string='Volume', default=0)
  base_product = fields.Char(string='Base')
  color_product = fields.Char(string='Color')
  technology_product = fields.Char(string='Technology')

  reference_product = fields.Char(
    string='Reference produit',
    compute='_compute_product_reference',
    store=True
  )

  def send_alerte_test(self):
    raise UserError('T\'es le meilleur')
  
  @api.depends(
    'format_product', 
    'volume_product', 
    'base_product', 
    'color_product', 
    'technology_product')
  def _compute_product_reference(self):
    for record in self:
      record.reference_product = f"{record.format_product or ''}{record.volume_product or ''}{record.base_product or ''}{record.color_product or ''}{record.technology_product or ''}"
