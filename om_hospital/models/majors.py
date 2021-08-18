# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Majors(models.Model):
    _name = 'om_hospital.doctor_majors'
    _description = "Hospital Doctor majors"
    _rec_name = "name"
    _sql_constraints = [
        ('name_unique', 'unique(name)', _("The name must be unique")),
    ]

    name = fields.Char(string=_("Name"), required=True)
    description = fields.Text(string=_("Description"))