from ferris import Controller, scaffold, messages, route_with
from ferris.components.upload import Upload
from ferris.controllers.download import Download
from ferris.components.search import Search
from google.appengine.api import app_identity
from app.models.event import Event
import logging
import json


class Events(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, messages.Messaging, Upload, Search, Download, )
        Model = Event

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete

    @route_with('/api/events/url', methods=['GET'])
    def url(self):
        return self.components.upload.generate_upload_url(
            uri=self.uri('events:complete')
        )

    @route_with('/api/events/complete', methods=['GET'])
    def complete(self):
        uploads = self.components.upload.get_uploads()
        for blobinfo in uploads:
            logging.info(blobinfo.filename)

        return 200

    @route_with('/api/events/download_url', methods=['GET'])
    def api_download_url(self, blobkey):
        return self.uri("download", blob=blobkey)

    @route_with('/api/events', methods=['GET'])
    def api_list(self):
        evt = Event.list_all()
        # logging.info("===EVT== 2:: %s" % evt)
        list_e = []
        for event in evt:
            if event.seat_map_url is None or event.seat_map_url == "":
                event.seat_map_url = "http://" + app_identity.get_default_version_hostname() + self.uri("download", blob=event.seat_map)
                event.put()

            if event.photo_url is None or event.photo_url == "":
                event.photo_url = "http://" + app_identity.get_default_version_hostname() + self.uri("download", blob=event.photo)
                event.put()
            list_e.append(event)

        evt_messages = Event.to_message(list_e)
        self.context['data'] = evt_messages

    @route_with('/api/events/:<e_key>/details', methods=['GET'])
    def api_ticket_details(self, e_key=None):
        evt = self.util.decode_key(e_key).get()
        if evt.seat_map_url is None or evt.seat_map_url == "":
            evt.seat_map_url = "http://" + app_identity.get_default_version_hostname() + self.uri("download", blob=evt.seat_map)
            evt.put()

        if evt.photo_url is None or evt.photo_url == "":
            evt.photo_url = "http://" + app_identity.get_default_version_hostname() + self.uri("download", blob=evt.photo)
            evt.put()

        evt_details = Event.find_event(evt)
        self.context['data'] = evt_details

    @route_with('/api/events/search/:<search_term>', methods=['GET'])
    def api_search(self, search_term=None):
        result = Event.search(search_term)
        self.context['data'] = result

    @route_with('/api/events/image_url', methods=['GET'])
    def api_uploads(self):
        evt = Event.query().get()
        uri = "http://" + app_identity.get_default_version_hostname() + self.uri("download", blob=evt.photo)
        return uri
