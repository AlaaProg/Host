from odoo import models, fields


class Booking(models.Model):
    _name = 'om_hospital.booking'
    _description = "Hospital Booking"
    _rec_name = "date"

    date = fields.Datetime(string="On Date", required=True)
    patient_id = fields.Many2one('om_hospital.patients', ondelete='cascade', string="Patient")
    doctor_id = fields.Many2one('om_hospital.doctors', ondelete='cascade', string="Doctor")
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, default='draft')


    def action_confirm(self):
        """Set state `confirm`"""
        self.state = 'confirm'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Appointment Confirmed... Thanks You',
                'type': 'rainbow_man',
            }
        }

    def action_done(self):
        """Set state `done`"""
        self.state = 'done'

    def action_cancel(self):
        """Set state `cancel`"""
        self.state = 'cancel'