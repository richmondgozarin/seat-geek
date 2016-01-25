from ferris import Controller, scaffold, messages, route_with
from ferris.components.pagination import Pagination
from ferris.components.upload import Upload
from ferris.controllers.download import Download
from app.models.ticket import Ticket
from app.models.event import Event
# import braintree
import logging
import json


class Tickets(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, Pagination, messages.Messaging, Upload, Download, )
        Model = Ticket
        pagination_limit = 10

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete

    @route_with('/api/tickets/upload_url', methods=['GET'])
    def url(self):
        return self.components.upload.generate_upload_url(
            uri=self.uri('tickets:complete')
        )

    @route_with('/api/tickets/complete', methods=['GET'])
    def complete(self):
        serving_urls = []
        sell_tickets = json.loads(self.request.body)
        event_key = self.util.decode_key(sell_tickets['event']).get()
        account = self.util.decode_key(sell_tickets['scalper_name']).get()

        uploads = self.components.upload.get_uploads()
        files = uploads.get('file')
        for blobinfo in files:

            logging.info('===::sell_tickets::=== %s' % type(account))
            params = {
                'event': event_key.key.urlsafe(),
                'scalper_name': account.key,
                'ticket_img': blobinfo.key(),
                'section': sell_tickets['section'],
                'quantity': sell_tickets['quantity'],
                'price': sell_tickets['price']
            }
            Ticket.create(params)
            # serving_urls.append({'filename': blobinfo.filename,
            #     'url': "https://storage.googleapis.com/%s" % (blobinfo.cloud_storage.gs_object_name[4:]),
            #     'content_type': blobinfo.content_type
            #     })

        return 200

    @route_with('/api/tickets/download_url', methods=['GET'])
    def api_download_url(self, blobkey):
        return self.uri("download", blob=blobkey)

    @route_with('/api/tickets', methods=['GET'])
    def api_list(self):
        self.context['data'] = Ticket.list_all()

    @route_with('/api/tickets', methods=['POST'])
    def api_create(self):
        sell_tickets = json.loads(self.request.body)
        event_key = self.util.decode_key(sell_tickets['event']).get()
        account = self.util.decode_key(sell_tickets['scalper_name']).get()
        params = {
            'event': event_key.key.urlsafe(),
            'scalper_name': account.key,
            'section': sell_tickets['section'],
            'quantity': sell_tickets['quantity'],
            'price': sell_tickets['price']
        }
        Ticket.create(params)
        return 200

    @route_with('/api/tickets/:<key>/seller', methods=['GET'])
    def api_seller_list(self, key=None):
        seller = self.util.decode_key(key).get()
        self.context['data'] = Ticket.list_per_user(seller.key)

    @route_with('/api/tickets/:<tckt_key>/deals', methods=['GET'])
    def api_get_ticket(self, tckt_key=None):
        deal = self.util.decode_key(tckt_key).get()
        deals = Ticket.find_tickets(deal.key)
        self.context['data'] = deals

    @route_with('/api/tickets/:<tckt_key>/details', methods=['GET'])
    def api_get_details(self, tckt_key=None):
        ticket = self.util.decode_key(tckt_key).get()
        # logging.info('===TICKETS == %s' % ticket)
        info = Ticket.to_message(ticket)
        self.context['data'] = info
