# from app.models.user import User, get_permission_level
from app.services.user_svc import UserSvc


class Permission:
    @staticmethod
    def current_user_is(comparator, role):
        user = UserSvc.get_current_user()
        current_user_role = user.is_seller if user else 'not logged in'
        import logging
        logging.info("::USER:: %s" % user)
        logging.info("::current_user_role:: %s" % current_user_role)
        if current_user_role:
            return True
        else:
            return False
