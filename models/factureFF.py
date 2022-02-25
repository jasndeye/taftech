from odoo import models,fields,api

class Factureclient(models.Model):
     _inherit = 'commerciale.factureclient'
     type=fields.Char(string='Facture Fasfood')