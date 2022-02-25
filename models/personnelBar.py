from odoo import models,fields,api

class Personnelbar(models.Model):
     _inherit = 'commerciale.personnel'
     type=fields.Char(string='Personnel Bar')