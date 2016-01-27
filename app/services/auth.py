# from ferris import settings
from app.errors import SeatNowError, clientForbiddenError
from app.services.permission import Permission
from google.appengine.api import users
import webapp2
import logging


def only(comparator, role):
    def inner(f):
        chain = getattr(f, 'authorizations', ())
        chain += (require_user(comparator, role),)
        setattr(f, 'authorizations', chain)
        return f
    return inner


def require_user(comparator, role):
    def inner(controller):
        try:
            if Permission.current_user_is(comparator, role):
                return True
            raise clientForbiddenError()
        except SeatNowError as e:
            logging.error(e)
            if controller.session.get('user', None):
                # build response
                resp = webapp2.Response()
                resp.status_int = e.code
                resp.status_message = e.description
                resp.body = e.description
                return resp
            else:
                return ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
    return inner
