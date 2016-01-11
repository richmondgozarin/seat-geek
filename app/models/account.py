from ferris import BasicModel, ndb
from google.appengine.api import app_identity
APP_ID = app_identity.get_application_id()


class Account(BasicModel):
    first_name = ndb.StringProperty(indexed=True)
    last_name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=False)

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @classmethod
    def list_all(cls):
        return cls.query()

    @classmethod
    def create(cls, params):
        item = cls()
        item.populate(**params)
        item.put()
        return item

    @classmethod
    def remove(cls):
        ndb.delete_multi(
            Account.query().fetch(keys_only=True)
        )

    @classmethod
    def get(cls, key_name, key_only=False):
        if not key_name:
            return None
        key = ndb.Key(cls, format_key_name(key_name))
        ret = key.get()
        if key_only:
            return key if ret else None
        return ret


def format_key_name(key_name):
    return str(key_name).replace(' ', '_').lower()
