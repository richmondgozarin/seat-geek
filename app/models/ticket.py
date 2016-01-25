from ferris import BasicModel, ndb, messages
from google.appengine.api import mail, app_identity
from app.models.id_tracker import IdTracker
from app.models.event import Event, EventMessage
APP_ID = app_identity.get_application_id()


class Ticket(BasicModel):
    event = ndb.KeyProperty(kind='Event', indexed=True)
    scalper_name = ndb.KeyProperty(kind='Account', indexed=True)
    ticket_img = ndb.BlobKeyProperty()
    ticket_url = ndb.StringProperty(indexed=True)
    section = ndb.StringProperty(indexed=True)
    quantity = ndb.IntegerProperty(indexed=True)
    price = ndb.FloatProperty(indexed=True)
    sold = ndb.BooleanProperty(default=False, indexed=True)


    @classmethod
    def list_all(cls):
        return cls.query(cls.sold == False).order(cls.price)

    @classmethod
    def list_per_user(cls, key):
        csas = cls.query(cls.scalper_name == key).order(cls.price)
        tickets = [cls.buildTicket(ticket) for ticket in csas]
        return CompletedTickets(tickets=tickets)

    @classmethod
    def create(cls, params):
        params['event'] = ndb.Key(urlsafe=params['event'])
        # params['ticket_number'] = IdTracker.generate_number('ticket')
        item = cls()
        item.populate(**params)
        item.put()
        return item

    @classmethod
    def remove(cls):
        ndb.delete_multi(
            Ticket.query().fetch(keys_only=True)
        )

    @classmethod
    def find_tickets(cls, key):
        csas = cls.find_all_by_event(key).filter(cls.sold == False).order(cls.price)
        tickets = [cls.buildTicket(ticket) for ticket in csas]
        return CompletedTickets(tickets=tickets)

    @classmethod
    def to_message(cls, entity):
        tickets = [cls.buildTicket(entity)]
        return CompletedTickets(tickets=tickets)

    @classmethod
    def buildTicket(cls, ticket):
        return TicketMessage(
            key=ticket.key.urlsafe(),
            section=ticket.section,
            quantity=ticket.quantity,
            price=ticket.price,
            scalper_name=cls.buildScalpers(ticket.scalper_name.get()),
            sold=ticket.sold,
            event=Event.buildEvent(ticket.event.get())
        )

    @classmethod
    def buildScalpers(cls, name):
        return ScalperMessage(
            key=name.key.urlsafe(),
            first_name=name.first_name,
            last_name=name.last_name,
            email=name.email
        )


class ScalperMessage(messages.Message):
    key = messages.StringField(1)
    first_name = messages.StringField(2)
    last_name = messages.StringField(3)
    email = messages.StringField(4)


class TicketMessage(messages.Message):
    key = messages.StringField(1)
    section = messages.StringField(2)
    quantity = messages.IntegerField(3)
    scalper_name = messages.MessageField(ScalperMessage, 4)
    price = messages.FloatField(5)
    sold = messages.BooleanField(6)
    event = messages.MessageField(EventMessage, 7)


class CompletedTickets(messages.Message):
    tickets = messages.MessageField(TicketMessage, 1, repeated=True)
