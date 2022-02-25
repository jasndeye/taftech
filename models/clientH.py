from odoo import models,fields,api

class Clienth(models.Model):
     _inherit = 'commerciale.client'
     type=fields.Char(string='Client Hotel')