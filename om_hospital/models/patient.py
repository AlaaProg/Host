# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'om_hospital.patients'
    _description = "Hospital Patients"
    _rec_name = "fullname"
    _sql_constraints = [
        ('phone_patient_unique', 'unique(phone)', "The phone number must be unique"),
    ]

    fullname = fields.Char(string='Full Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(string='Gender',
                              selection=[
                                 ('male', 'Male'),
                                 ('kid', 'Kid'),
                                 ('female', 'Female'),
                              ], default='kid')
    description = fields.Text(string='Description')
    booking_ids = fields.One2many('om_hospital.booking',
                                  'patient_id',
                                  string="Appointemnts")

