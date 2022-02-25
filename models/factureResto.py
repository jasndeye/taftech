from odoo import models,fields,api

class Factureclientresto(models.Model):
    _inherit = 'commerciale.factureclient'
    type=fields.Char(string='Facture Resto')