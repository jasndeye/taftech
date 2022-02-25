from odoo import models,fields,api

class Paiementresto(models.Model):
      _inherit = 'commerciale.paiement'
      type=fields.Char(string='Paiement Resto')