# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'om_hospital.doctors'
    _description = _("Hospital doctors")
    _rec_name = "fullname"
    _sql_constraints = [

        ('phone_unique', 'unique(phone)', _("The phone number must be unique")),
        ('email_unique', 'unique(email)', _("The email address must be unique")),
    ]

    fullname = fields.Char(string=_("Full Name"), required=True)
    phone = fields.Char(string=_("Phone Number"), required=True)
    avatar = fields.Binary(string=_("Avatar"), required=True)
    email = fields.Char(string=_("E-mail Address"))
    booking_ids = fields.One2many('om_hospital.booking', 'doctor_id',
                                    string=_("Appointemnts"))
    majors_ids = fields.Many2many('om_hospital.doctor_majors', string=_("Majors"), required=True, store=True)
    user_id = fields.Many2one('res.users', string=_('Manager User'))

    def validate_email(self, email: str) -> bool:
        """Validate Email
            :param str email: Email Address
            :return: Email status is valid or invalid
            :rtype: bool
        """
        return bool(re.match(r'^[\.\_a-z0-9-]+@[a-z0-9-]+(\.[a-z]{2,4})$', email))

    @api.constrains('email')
    def validate(self):
        """Validate model fields"""
        if self.email:
            if not self.validate_email(self.email):
                raise ValidationError('E-mail invalid')