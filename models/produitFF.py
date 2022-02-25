from odoo import models,fields,api

class Produitff(models.Model):
     _inherit = 'commerciale.produit'
     type=fields.Char(string='Produit Fasfood')
     