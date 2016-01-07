from ferris import Model, ndb


class IdTracker(Model):

    ticket_number = ndb.IntegerProperty(required=True, default=0)
    event_number = ndb.IntegerProperty(required=True, default=0)

    @staticmethod
    def generate_number(tracker_name, width=9):
        instance = ndb.Key(IdTracker, tracker_name).get()
        if not instance:
            instance = IdTracker(id=tracker_name)
        if tracker_name == 'ticket':
            instance.ticket_number += 1
        elif tracker_name == 'event':
            instance.event_number += 1
        instance.put()
        if tracker_name == 'ticket':
            return str(instance.ticket_number).zfill(width)
        return str(instance.event_number).zfill(width)
