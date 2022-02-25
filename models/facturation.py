from odoo import models,fields,api

class Facturation(models.Model):
     _inherit = 'commerciale.factureclient'
     type=fields.Char(string='Facture hotel')