from odoo import models, fields

class ProtocolAssignment(models.Model):
    _name = "cancer_center.protocol.assignment"
    _description = "Chemotherapy protocol assignment"

    patient_id = fields.Many2one('cancer_center.patient', string='patient')
    protocol_id = fields.Many2one('cancer_center.protocol', string='protocol')
    protocol_assignment_detail_ids = fields.One2many('cancer_center.protocol.assignment.detail', 
                                             'protocol_assignment_id', 
                                              string='prot_assig_detail')

    date_start = fields.Date(string="Start Date", required=True)
    interval = fields.Integer('interval')



