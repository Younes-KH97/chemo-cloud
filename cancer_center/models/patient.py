from odoo import models, fields

class Patient(models.Model):
    _name = "cancer_center.patient"
    name = fields.Char()
    dob = fields.Date()
    address_of_residence = fields.Char() # Make a Select from a json of wilayas
    phone_number = fields.Char()

    protocols_ids = fields.Many2many('cancer_center.protocol', string='protocols')