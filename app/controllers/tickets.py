from ferris import Controller, scaffold, messages, route_with
from ferris.components.pagination import Pagination
from ferris.components.upload import Upload
from app.models.ticket import Ticket
from app.models.event import Event
import braintree
import logging


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

    @route_with('/api/tickets/:<e_key>/deals', methods=['GET'])
    def api_get_tickets(self, e_key=None):
        deal = self.util.decode_key(e_key).get()
        deals = Ticket.find_tickets(deal.key)
        self.context['data'] = deals


    @classmethod
    def braintree(self):
        braintree.Configuration.configure(
            braintree.Environment.Sandbox,
            'kqg558ff2r98njfx',
            'dqq36p9vf7nprsxz',
            '5d570f06244e40d9d2a78159edb748ab'
        )

    @route_with("/api/braintree/client_token", methods=["GET"])
    def client_token():
        return braintree.ClientToken.generate()

    @route_with("/api/braintree/checkout", methods=["POST"])
    def create_purchase():
      nonce = request.form["payment_method_nonce"]
      result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce_from_the_client
    })
