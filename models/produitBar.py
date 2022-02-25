from odoo import models,fields,api

class Produitbar(models.Model):
     _inherit = 'commerciale.produit'
     type=fields.Char(string='Produit Bar')
