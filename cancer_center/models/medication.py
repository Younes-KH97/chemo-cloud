from odoo import models, fields

class Medication(models.Model):
    _name = "cancer_center.medication"
    _description = "Chemotherapy medication"

    protocol_assignment_detail_ids = fields.One2many('cancer_center.protocol.assignment.detail', 
                                             'madication_id', 
                                              string='prot_assig_detail')

    name = fields.Char()
    posology = fields.Float('posology')