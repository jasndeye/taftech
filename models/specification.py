from odoo import models,fields,api

class Specification(models.Model):
     _name = 'taftech.specification'
     
     nom=fields.Char(string="Spécification")