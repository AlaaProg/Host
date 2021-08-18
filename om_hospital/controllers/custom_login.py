import odoo
from odoo.tools.translate import _
from datetime import datetime
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import ensure_db, _get_login_redirect_url


class CustomLogin(http.Controller):

    def _login_redirect(self, uid, redirect=None):
        return _get_login_redirect_url(uid, redirect)

    @http.route('/web/login', type='http', auth='public')
    def get_form_login(self, redirect=None, **kw):
        """Get form login """
        ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and http.request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            try:
                uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
                return http.redirect_with_hash(self._login_redirect(uid, redirect=redirect))
            except odoo.exceptions.AccessDenied as e:
                request.uid = old_uid
                if e.args == odoo.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employees can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
            values['disable_database_manager'] = True

        response = http.request.render('om_hospital.web_custom_login', values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response
