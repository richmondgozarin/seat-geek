from ferris import Controller, messages, route_with
from app.models.ticket import Ticket
import paypalrestsdk
import json
import logging


class PaypalPayments(Controller):
    class Meta:
        prefixes = ('api',)
        components = (messages.Messaging,)
        Model = Ticket

    @route_with('/api/paypal/access_token', methods=['GET'])
    def api_paypal_payment(self):

        my_api = paypalrestsdk.Api({
            'mode': 'sandbox',
            'client_id': 'EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM',
            'client_secret': 'EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM'
        })

        logging.info('PAY: %s' % type(my_api))
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "localhost:8080/#/main/python?success=true",
                "cancel_url": "localhost:8080/#/main/python?cancel=true"},

            "transactions": [{
                "amount": {
                    "total": "1200",
                    "currency": "PHP"
                },
                "description": "creating a payment"
            }]
        }, api=my_api)

        if payment.create():
            print("Payment created successfully")
            return 200
        else:
            print(payment.error)
            return 200
        # self.context['data'] = ''
