from datetime import datetime
from odoo import http
from .controllers import allowed_method


class OmHospital(http.Controller):

    def create_appointment(self, kw: dict) -> object:
        """Create Appintment"""
        try:
            return http.request.env['om_hospital.booking'].create({
                "doctor_id": kw.get("doctor_id"),
                'date':  datetime.strptime(kw.get("date"), "%Y-%m-%dT%H:%M"),
            }), True
        except Exception as err:
            return err, False

    def create_patient(self, kw: dict) -> object:
        """Create new patient"""
        try:
            return http.request.env['om_hospital.patients'].create({
                "fullname": kw.get("fullname"),
                "phone": kw.get("phone"),
                "age": kw.get("age"),
                "gender": kw.get("gender"),
                "description": kw.get("description"),
            }), True
        except Exception as err:
            return err, False

    def find_patient_by_phone(self, phone: str) -> object:
        """Find patient by phone number"""
        if not phone:
            return None
        return http.request.env['om_hospital.patients'].sudo().search([['phone', '=', phone]])

    @http.route('/appointment/', type='http', auth='public', website=True)
    def get_form_appointment(self, **kw):
        """Get form appointment """

        # get all doctors
        doctors = http.request.env['om_hospital.doctors'].sudo().search([])

        return http.request.render('om_hospital.appointment_create_form',
                                   {"doctors": doctors})

    @allowed_method("POST", redirect='/appointment/')
    @http.route('/appointment/create/', auth='public', website=True)
    def post_appointment(self, **kw):
        """Post form appointment"""

        # create appointment
        appointment, ok = self.create_appointment(kw)
        # get patient
        patient = self.find_patient_by_phone(kw.get("phone"))
        if not patient: # if not None
            patient, ok = self.create_patient(kw) # create new patient

        # set patient `Id` to appointment `many2one`
        appointment.write({'patient_id': patient.id})

        return http.request.render('om_hospital.appointment_view', {'patient': patient})