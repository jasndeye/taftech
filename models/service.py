from odoo import models,fields,api

class Service(models.Model):
     _name = 'taftech.service'

     nom=fields.Char(string="Nom", required=True)
     image= fields.Binary(string="Photo", required=True)
     description= fields.Text(string="description", required=True)
     tarif_horaire= fields.Float(string="Tarif horaire", required=True)
