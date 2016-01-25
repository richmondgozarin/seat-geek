"""
This file is used to configure application settings.

Do not import this file directly.

You can use the settings API via:

    from ferris import settings

    mysettings = settings.get("mysettings")

The settings API will load the "settings" dictionary from this file. Anything else
will be ignored.

Optionally, you may enable the dynamic settings plugin at the bottom of this file.
"""

settings = {}

settings['timezone'] = {
    'local': 'US/Eastern'
}

settings['email'] = {
    # Configures what address is in the sender field by default.
    'sender': None
}

settings['app_config'] = {
    'webapp2_extras.sessions': {
        # WebApp2 encrypted cookie key
        # You can use a UUID generator like http://www.famkruithof.net/uuid/uuidgen
        'secret_key': '9a788030-837b-11e1-b0c4-0800200c9a66',
    }
}

settings['oauth2'] = {
    # OAuth2 Configuration should be generated from
    # the google cloud console (Credentials for Web Application)
    'client_id': None,  # XXXXXXXXXXXXXXX.apps.googleusercontent.com
    'client_secret': None,
    'developer_key': None  # Optional
}

settings['oauth2_service_account'] = {
    # OAuth2 service account configuration should be generated
    # from the google cloud console (Service Account Credentials)
    'client_email': None,  # XXX@developer.gserviceaccount.com
    'private_key': None,  # Must be in PEM format
    'developer_key': None  # Optional
}

settings['upload'] = {
    # Whether to use Cloud Storage (default) or the blobstore to store uploaded files.
    'use_cloud_storage': True,
    # The Cloud Storage bucket to use. Leave as "None" to use the default GCS bucket.
    # See here for info: https://developers.google.com/appengine/docs/python/googlecloudstorageclient/activate#Using_the_Default_GCS_Bucket
    'bucket': None
}

# Enables or disables app stats.
# Note that appstats must also be enabled in app.yaml.
settings['appstats'] = {
    'enabled': False,
    'enabled_live': False
}

# settings for app
settings['paypal'] = {
    # 'endpoint': 'https://api-3t.sandbox.paypal.com/nvp',  # sandbox xpress-checkout
    'endpoint': 'https://svcs.sandbox.paypal.com/AdaptivePayments/',  # sandbox
    # 'endpoint': 'https://svcs.paypal.com/AdaptivePayments/', # production
    'payment_host': 'https://www.sandbox.paypal.com/au/cgi-bin/webscr',  # sandbox
    # 'payment_host': 'https://www.sandbox.paypal.com/cgi-bin/webscr',  # sandbox xpress-checkout
    # 'payment_host': 'https://www.paypal.com/webscr', # production
    'userid': 'richmond.gozarin-facilitator_api1.gmail.com',
    'password': '3JSA3MY7GYQNARJK',
    'signature': 'AOsWznKk3.jdTvQdGOlADSuc1T1MAb1WUBTsNrEU9DlE7u9hYhU9lgsX',
    'app_id': 'APP-80W284485P519543T',  # sandbox only
    'email': 'richmond.gozarin-facilitator@gmail.com',

    'commission': 1.10,  # 10%

    'use_chain': False,
    'use_ipn': False,
    'use_embedded': False,
    'shipping': False,  # not yet working properly; PayPal bug

    # 'embedded_endpoint': 'https://paypal.com/webapps/adaptivepayment/flow/pay'
    'embedded_endpoint': 'https://www.sandbox.paypal.com/webapps/adaptivepayment/flow/pay'
}

# Optionally, you may use the settings plugin to dynamically
# configure your settings via the admin interface. Be sure to
# also enable the plugin via app/routes.py.

#import plugins.settings

# import any additional dynamic settings classes here.

# import plugins.my_plugin.settings

# Un-comment to enable dynamic settings
#plugins.settings.activate(settings)
