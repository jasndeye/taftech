from email.policy import default
from odoo import models,fields,api

class Clientbar(models.Model):
     _inherit = 'commerciale.client'
     type=fields.Char(string='Client Bar')
     
