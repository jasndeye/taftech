from odoo import models,fields,api

class Reservation(models.Model):
     _name = 'taftech.reservation'
     
     date_deb=fields.Datetime(string="Date de Debut")
     date_fin=fields.Datetime(string="Date de Fin")
     prix=fields.Float(string="Prix de la reservation")
     etat=fields.Selection([('r','reservé'),('v','validé'),('t','terminé'),('a','annulé')], string="Etat de la réservation")
     chambre_ids=fields.Many2many('taftech.chambre', string='Chambres')