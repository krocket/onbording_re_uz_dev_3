from odoo import fields, models, api
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ReuzSalesOrder(models.Model):
  _inherit = 'sale.order'

  silver_reference = fields.Char(string='Silver reference')
  planned_date = fields.Date(string='Date de plannification')
  format_product = fields.Char(string='Format produit')
  volume_product = fields.Int(string='Volume produit')
  base_product = fields.Char(string='Base produit')
  color_product = fields.Char(string='Color produit')
  technology_product = fields.Char(string='Technology produit')

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
    return f"{self.format_product}{self.volume_product}{self.base_product}{self.color_product}{self.technology_product}"
