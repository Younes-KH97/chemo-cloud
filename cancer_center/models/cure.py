from odoo import models, fields

class Cure(models.Model):
    _name = "cancer_center.cure"
    _description = "Chemotherapy cure"

    protocol_assignment_id = fields.Many2one('cancer_center.protocol.assignment', 
                                             string='protocol_assignment')
    
    tall = fields.Float('tall')
    weight = fields.Float('weight')
    dose = fields.Float('dose')
    note = fields.Text('note')
    date_of_cure = fields.Date('date_of_cure')
    medication_id = fields.Many2one('cancer_center.medication', string='medication')