from odoo import models,fields,api

class Commandeclientbar(models.Model):
     _inherit = 'commerciale.commandeclient'
     type=fields.Char(string='Commande Bar')
     
    