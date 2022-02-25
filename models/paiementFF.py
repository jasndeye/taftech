from odoo import models,fields,api

class Paiementff(models.Model):
     _inherit = 'commerciale.paiement'
     type=fields.Char(string='Paiement Fasfood')