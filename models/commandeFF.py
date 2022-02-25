from odoo import models,fields,api

class Commandeclientff(models.Model):
     _inherit = 'commerciale.commandeclient'
     type=fields.Char(string='Commande Fasfood')