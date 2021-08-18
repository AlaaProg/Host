# -*- coding: utf-8 -*-
import functools
from odoo import http

def allowed_method(method, redirect="/"):
    """POST method allowed"""
    def decorator(f):
        @functools.wraps(f)
        def response(*args, **kw):
            if http.request.httprequest.method != method:
                return http.request.redirect(redirect)

            return f(*args, **kw)
        return response
    return decorator