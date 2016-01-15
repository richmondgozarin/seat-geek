from ferris import Controller, scaffold, messages, route_with
from ferris.components.pagination import Pagination
from ferris.components.upload import Upload
from app.models.ticket import Ticket
from app.models.event import Event
# import braintree
import logging
import json


class Tickets(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, Pagination, messages.Messaging, Upload)
        Model = Ticket
        pagination_limit = 10

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete

    @route_with('/api/tickets', methods=['GET'])
    def api_list(self):
        self.context['data'] = Ticket.list_all()

    @route_with('/api/tickets', methods=['POST'])
    def api_create(self):
        sell_tickets = json.loads(self.request.body)
        event_key = self.util.decode_key(sell_tickets['event']).get()
        account = self.util.decode_key(sell_tickets['scalper_name']).get()
        logging.info('===::sell_tickets::=== %s' % type(account))
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

    # @classmethod
    # def braintree(self):
    #     braintree.Configuration.configure(
    #         braintree.Environment.Sandbox,
    #         'kqg558ff2r98njfx',
    #         'dqq36p9vf7nprsxz',
    #         '5d570f06244e40d9d2a78159edb748ab'
    #     )

    # @route_with("/api/braintree/client_token", methods=["GET"])
    # def client_token():
    #     return braintree.ClientToken.generate()

    # @route_with("/api/braintree/checkout", methods=["POST"])
    # def create_purchase():
    #   nonce = request.form["payment_method_nonce"]
    #   result = braintree.Transaction.sale({
    #     "amount": "10.00",
    #     "payment_method_nonce": nonce_from_the_client
    # })
