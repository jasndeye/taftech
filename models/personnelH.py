from odoo import models,fields,api
from datetime import date

class Personnelh(models.Model):
     _inherit = 'commerciale.personnel'
     type=fields.Char(string='Personnel Hotel')