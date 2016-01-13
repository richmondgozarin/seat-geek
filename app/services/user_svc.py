from google.appengine.api import users
from app.models.account import Account


class UserSvc:

    @staticmethod
    def get_current_user():
        user = users.get_current_user()
        return Account.get(key_name=user.email())

    @staticmethod
    def generate_logout_url():
        return users.create_logout_url('/')
