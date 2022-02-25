# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Menuresto(models.Model):

     _inherit = 'commerciale.menu'
     type=fields.Char(string='Menu Resto')