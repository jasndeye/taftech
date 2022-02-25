from odoo import models,fields,api

class Paiementbar(models.Model):
     _inherit = 'commerciale.paiement'
     type=fields.Char(string='Paiement Bar')
     