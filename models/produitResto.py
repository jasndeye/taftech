from odoo import models,fields,api

class Produitresto(models.Model):
     _inherit = 'commerciale.produit'
     type=fields.Char(string='Produit Resto')