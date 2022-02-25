from odoo import models,fields,api

class Commandeclientresto(models.Model):
     _inherit = 'commerciale.commandeclient'
     type=fields.Char(string='Commande Resto')