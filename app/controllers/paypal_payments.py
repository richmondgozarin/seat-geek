from ferris import Controller, messages, route_with
from google.appengine.api import users
from ferris import settings
from app.models.ticket import Ticket
from app.models.purchase import Purchase
import app.services.utils as utils
import app.services.paypal as paypal
import json
import logging


class PaypalPayments(Controller):
    class Meta:
        prefixes = ('api',)
        components = (messages.Messaging,)
        Model = Ticket

    @route_with('/api/paypal/:<key>', methods=['POST'])
    def post(self, key):
        item = self.util.decode_key(key).get()
        (ok, pay) = self.start_purchase(item)
        logging.info('OK:: %s' % ok)
        if ok:
            logging.info('PAY:: %s' % pay.next_url().encode('ascii'))
            return pay.next_url().encode('ascii')  # self.redirect(  ) # go to paypal
        else:
            data = {
                'item': Ticket.get(key),
                'message': 'An error occurred during the purchase process'
            }
            utils.add_user(self.request.uri, data)
            self.context['data'] = data

    def start_purchase(self, item):
        account = self.util.decode_key(item.scalper_name).get()
        params = {
            'item': item.key,
            'owner': account.email,
            'purchaser': users.get_current_user(),
            'status': 'NEW',
            'secret': utils.random_alnum(16)
        }
        purchase = Purchase.create(params)
        if settings.get('paypal').get('use_ipn'):
            ipn_url = "%s/ipn/%s/%s/" % (self.request.host_url, purchase.key(), purchase.secret)
        else:
            ipn_url = None
        if settings.get('paypal').get('use_chain'):
            seller_paypal_email = utils.paypal_email(account.email)
        else:
            seller_paypal_email = None

        pay = paypal.Pay(
            item.price,
            "%s" % (self.request.uri),
            # "%sreturn/%s/%s/" % (self.request.uri, purchase.key, purchase.secret),
            "%s" % (self.request.uri),
            # "%scancel/%s/" % (self.request.uri, purchase.key),
            self.request.remote_addr,
            seller_paypal_email,
            ipn_url,
            shipping=settings.get('paypal').get('shipping'))

        purchase.debug_request = pay.raw_request
        purchase.debug_response = pay.raw_response
        purchase.paykey = pay.paykey()
        purchase.put()

        if pay.status() == 'CREATED':
            purchase.status = 'CREATED'
            purchase.put()
            item.sold = True
            item.put()
            return (True, pay)
        else:
            purchase.status = 'ERROR'
            purchase.put()
            return (False, pay)

# class BuyReturn(RequestHandler):

#   def get(self, item_key, purchase_key, secret ):
#     '''user arrives here after purchase'''
#     purchase = model.Purchase.get( purchase_key )

#     # validation
#     if purchase == None: # no key
#       self.error(404)

#     elif purchase.status != 'CREATED' and purchase.status != 'COMPLETED':
#       purchase.status_detail = 'Expected status to be CREATED or COMPLETED, not %s - duplicate transaction?' % purchase.status
#       purchase.status = 'ERROR'
#       purchase.put()
#       self.error(501)

#     elif secret != purchase.secret:
#       purchase.status = 'ERROR'
#       purchase.status_detail = 'BuyReturn secret "%s" did not match' % secret
#       purchase.put()
#       self.error(501)

#     else:
#       if purchase.status != 'COMPLETED':
#         purchase.status = 'RETURNED'
#         purchase.put()

#       if settings.SHIPPING:
#         purchase.shipping = paypal.ShippingAddress( purchase.paykey, self.request.remote_addr ).raw_response # TODO parse
#         purchase.put()

#       data = {
#         'item': model.Item.get(item_key),
#         'message': 'Purchased',
#       }

#       utils.add_user( self.request.uri, data )

#       if settings.USE_EMBEDDED:
#         data['close_embedded'] = True
#         data['items'] = model.Item.recent()
#         path = os.path.join(os.path.dirname(__file__), 'templates/main_embedded.htm')
#       else:
#         path = os.path.join(os.path.dirname(__file__), 'templates/buy.htm')
#       self.response.out.write(template.render(path, data))

# class BuyCancel(RequestHandler):
#   def get(self, item_key, purchase_key):
#     logging.debug( "cancelled %s with %s" % ( item_key, purchase_key ) )
#     purchase = model.Purchase.get( purchase_key )
#     purchase.status = 'CANCELLED'
#     purchase.put()
#     data = {
#       'item': model.Item.get(item_key),
#       'message': 'Purchase cancelled',
#     }
#     utils.add_user( self.request.uri, data )
#     if settings.USE_EMBEDDED:
#       data['close_embedded'] = True
#       data['items'] = model.Item.recent()
#       path = os.path.join(os.path.dirname(__file__), 'templates/main_embedded.htm')
#     else:
#       path = os.path.join(os.path.dirname(__file__), 'templates/buy.htm')
#     self.response.out.write(template.render(path, data))
