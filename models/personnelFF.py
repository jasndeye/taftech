from odoo import models,fields,api

class Personnelff(models.Model):
     _inherit = 'commerciale.personnel'
     type=fields.Char(string='Personnel Fasfood')