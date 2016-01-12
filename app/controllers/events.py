from ferris import Controller, scaffold, messages, route_with
from ferris.components.upload import Upload
from ferris.components.search import Search
from app.models.event import Event
import logging


class Events(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, messages.Messaging, Upload, Search,)
        Model = Event

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete

    @route_with('/api/events', methods=['GET'])
    def api_list(self):
        self.context['data'] = Event.list_all()

    @route_with('/api/events/:<e_key>/details', methods=['GET'])
    def api_ticket_details(self, e_key=None):
        evt = self.util.decode_key(e_key).get()
        evt_details = Event.find_event(evt)
        self.context['data'] = evt_details

    @route_with('/api/events/search/:<search_term>', methods=['GET'])
    def api_search(self, search_term=None):
        result = Event.search(search_term)
        self.context['data'] = result

    @route_with('/api/events/image_url', methods=['GET'])
    def api_uploads(self):
        uploads = self.components.upload.get_uploads()
        for blobinfo in uploads:
            logging.info(blobinfo.filename)
        return 200
