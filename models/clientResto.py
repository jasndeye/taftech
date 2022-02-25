from email.policy import default
from odoo import models,fields,api

class Clientresto(models.Model):
       _inherit = 'commerciale.client'
       type=fields.Char(string='Client Resto')