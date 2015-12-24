from ferris import BasicModel, ndb


class Subscription(BasicModel):


    @classmethod
    def create(cls, params):
        item = cls()
        item.populate(**params)
        item.put()
        return item
