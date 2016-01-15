from ferris import BasicModel, ndb, messages
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
    def get(cls, key_name=None):
        if key_name:
            return cls.find_by_email(key_name)
        else:
            return None

    @staticmethod
    def transform_message(entity):
        return EventMessage(
            key=entity.key.urlsafe(),
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email
        )


def format_key_name(key_name):
    return str(key_name).replace(' ', '_').lower()


class EventMessage(messages.Message):
    key = messages.StringField(1)
    first_name = messages.StringField(2)
    last_name = messages.StringField(3)
    email = messages.StringField(4)
