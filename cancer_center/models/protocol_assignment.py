from odoo import models, fields, api
from datetime import date, timedelta, datetime

class ProtocolAssignment(models.Model):
    _name = "cancer_center.protocol.assignment"
    _description = "Chemotherapy protocol assignment"

    patient_id = fields.Many2one('cancer_center.patient', string='patient')
    protocol_id = fields.Many2one('cancer_center.protocol', string='protocol')
    protocol_assignment_detail_ids = fields.One2many('cancer_center.protocol.assignment.detail', 
                                             'protocol_assignment_id', 
                                              string='prot_assig_detail')
    cure_ids = fields.One2many('cancer_center.cure', 'protocol_assignment_id', string='cures')
    

    date_start = fields.Date(string="Start Date", required=True)
    interval = fields.Integer('interval')
    number_of_cures = fields.Integer('number_of_cures')
    

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            interval = val["interval"]
            date_start = val["date_start"]
            curr_date = datetime.strptime(date_start, '%Y-%m-%d').date()
            number_of_cures = val["number_of_cures"]
            for i in range(number_of_cures):
                for protocol_detail in val['protocol_assignment_detail_ids']:
                    self.env["cancer_center.cure"].create({
                        "medication_id": protocol_detail[2]["medication_id"],
                        "weight": 66.0,
                        "date_of_cure": curr_date
                    })
                    curr_date = curr_date + timedelta(days=protocol_detail[2]["day_number"])
                curr_date = curr_date + timedelta(days=interval)
        return super().create(val)


    def show_planning(self):
        pass