from ferris import BasicModel, ndb, messages
from ferris.behaviors import searchable
from google.appengine.ext import deferred
from google.appengine.api import app_identity
from app.models.id_tracker import IdTracker

import logging
import urllib2
APP_ID = app_identity.get_application_id()


class Event(BasicModel):
    class Meta:
        behaviors = (searchable.Searchable,)
        search_index = ('index')
        search_fields = ('event_name', 'artist', 'venue',)

    event_number = ndb.StringProperty(indexed=True)
    event_name = ndb.StringProperty(indexed=True)
    artist = ndb.StringProperty(indexed=True)
    description = ndb.StringProperty(indexed=True)
    schedule_date = ndb.DateProperty(indexed=True)
    schedule_time = ndb.StringProperty(indexed=True)
    venue = ndb.StringProperty(indexed=True)
    location = ndb.StringProperty(indexed=True)
    external_link = ndb.StringProperty(indexed=True)
    photo = ndb.BlobKeyProperty()
    photo_url = ndb.StringProperty(indexed=True)
    seat_map = ndb.BlobKeyProperty()
    seat_map_url = ndb.StringProperty(indexed=True)

    def create_index(self):
        deferred.defer(EventIndex.create, self)

    def after_put(self, key):
        self.create_index()

    def __repr__(self):
        return self.event_name

    @classmethod
    def list_all(cls):
        return cls.query().fetch()

    @classmethod
    def to_message(cls, events):
        eventMsg = [cls.buildEvent(event) for event in events]
        return CompletedEvents(events=eventMsg)

    @classmethod
    def create(cls, params):
        params['event_number'] = IdTracker.generate_number('event')
        item = cls()
        item.populate(**params)
        item.put()
        return item

    @classmethod
    def update(cls, **params):
        item = cls()
        item.populate(**params)
        item.put()

    @classmethod
    def remove(cls):
        ndb.delete_multi(
            Event.query().fetch(keys_only=True)
        )

    @classmethod
    def search(cls, query_string=None, limit=50):
        try:
            query = EventIndex.query()

            if query_string:
                query_string = query_string.lower()
                query = query.filter(EventIndex.typeahead_list >= query_string, EventIndex.typeahead_list < query_string + u"\ufffd")

            results = query.fetch(limit, keys_only=True)
            results = ndb.get_multi([x.parent() for x in results])

            events = [cls.buildEvent(event) for event in results]
            return CompletedEvents(events = events)
        except urllib2.HttpError, e:
            return []

    @classmethod
    def find_event(cls, event):
        events = [cls.buildEvent(event)]
        return CompletedEvents(events=events)

    @classmethod
    def buildEvent(cls, event):
        return EventMessage(
            key=event.key.urlsafe(),
            event_name=event.event_name,
            description=event.description,
            schedule_date='{0:%B} {0.day}, {0.year}'.format(event.schedule_date),
            schedule_time=event.schedule_time,
            venue=event.venue,
            location=event.location,
            external_link=event.external_link,
            photo_url=event.photo_url,
            seat_map_url=event.seat_map_url
        )


class EventIndex(ndb.Model):
    typeahead_list = ndb.StringProperty(repeated=True, indexed=True)

    @classmethod
    def create(cls, event):
        try:
            l = event.event_name.split(' ')
            m = event.venue.split(' ')
            l.extend(m)
            l = set([x.lower() for x in l])
            typeahead_list = l

        except Exception, e:
            logging.info(e)

        try:
            cls(parent=event.key, id='idx', typeahead_list=typeahead_list).put()
        except Exception, e:
            logging.exception(e)
            pass


class EventMessage(messages.Message):
    event_name = messages.StringField(1)
    description = messages.StringField(2)
    schedule_date = messages.StringField(3)
    schedule_time = messages.StringField(4)
    venue = messages.StringField(5)
    location = messages.StringField(6)
    external_link = messages.StringField(7)
    key = messages.StringField(10)
    photo_url = messages.StringField(8)
    seat_map_url = messages.StringField(9)


class CompletedEvents(messages.Message):
    events = messages.MessageField(EventMessage, 1, repeated=True)

