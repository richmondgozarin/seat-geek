from ferris import BasicModel, ndb


class Subscription(BasicModel):
    premium = ndb.KeyProperty(kind="Account", indexed=True)
    email = ndb.StringProperty(required=True, indexed=True)
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    subscription = ndb.StringProperty(indexed=False)

    @classmethod
    def list_all(cls):
        return cls.query()

    @classmethod
    def create(cls, params):
        params['premium'] = ndb.Key(urlsafe=params['premium'])
        item = cls()
        item.populate(**params)
        item.put()
        return item

    @classmethod
    def remove(cls):
        ndb.delete_multi(
            Subscription.query().fetch(keys_only=True)
        )
