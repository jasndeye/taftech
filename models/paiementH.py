from odoo import models,fields,api

class Paiementh(models.Model):
     _inherit = 'commerciale.paiement'
     type=fields.Char(string='Paiement Hotel')
     