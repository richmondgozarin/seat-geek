from ferris import BasicModel, ndb


class Subscription(BasicModel):
    email = ndb.StringProperty(required=True, indexed=True)
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    subscription = ndb.StringProperty(indexed=False)

    @classmethod
    def create(cls, params):
        item = cls()
        item.populate(**params)
        item.put()
        return item
