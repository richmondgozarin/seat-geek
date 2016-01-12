from google.appengine.api import users
from app.models.account import Account


class UserSvc:

    @staticmethod
    def get_current_user(key_only=False):
        user = users.get_current_user()
        return Account.get(user.email(), key_only=key_only)

    @staticmethod
    def generate_logout_url():
        return users.create_logout_url('/')
