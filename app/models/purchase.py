from google.appengine.ext import ndb
from ferris import BasicModel


class Purchase(ndb.Model):
    '''a completed transaction'''
    item = ndb.KeyProperty(kind='Ticket', indexed=True)
    owner = ndb.StringProperty(indexed=True)
    purchaser = ndb.UserProperty(indexed=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    status = ndb.StringProperty( choices=( 'NEW', 'CREATED', 'ERROR', 'CANCELLED', 'RETURNED', 'COMPLETED' ) )
    status_detail = ndb.StringProperty()
    secret = ndb.StringProperty() # to verify return_url
    debug_request = ndb.TextProperty()
    debug_response = ndb.TextProperty()
    paykey = ndb.StringProperty()
    shipping = ndb.TextProperty()

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
            Purchase.query().fetch(keys_only=True)
        )
