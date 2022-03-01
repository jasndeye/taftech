from odoo import models,fields,api

class Specification(models.Model):
     _name = 'taftech.specification'
     
     name=fields.Char(string="Spécification")
     chambre_ids=fields.Many2many('taftech.chambre')