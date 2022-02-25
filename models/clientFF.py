from email.policy import default
from odoo import models,fields,api

class Clientff(models.Model):
     _inherit = 'commerciale.client'
     type=fields.Char(string='Client Fasfood')