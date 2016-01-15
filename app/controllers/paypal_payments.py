from ferris import Controller, messages, route_with
from app.models.ticket import Ticket
import paypalrestsdk
import json


class PaypalPayments(Controller):
    class Meta:
        prefixes = ('api',)
        components = (messages.Messaging,)
        Model = Ticket

    @route_with('/api/paypal/access_token', methods=['GET'])
    def api_paypal_payment(self):
        pay = paypalrestsdk.configure({
            'mode': 'sandbox',
            'client_id': 'EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM',
            'client_secret': 'EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM'
        })



        # payment = paypalrestsdk.Payment({
        #     "intent": "sale",
        #     "payer": {
        #         "payment_method": "paypal"
        #     },
        #     "redirect_urls": {
        #         "return_url": "https://devtools-paypal.com/guide/pay_paypal/python?success=true",
        #         "cancel_url": "https://devtools-paypal.com/guide/pay_paypal/python?cancel=true"},

        #     "transactions": [{
        #         "amount": {
        #             "total": "12",
        #             "currency": "USD"
        #         },
        #         "description": "creating a payment"
        #     }]
        # })

        # pay = payment.create()

        self.context['data'] = pay
