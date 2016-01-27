from ferris.core.ndb.util import decode_key as decode
from google.appengine.api import users
from app.models.account import Account
import json
import random
import string


def json_loads(request_body, keys):
    params = json.loads(request_body)

    def inner(key):
        if key not in params:
            return
        if isinstance(params[key], list):
            params[key] = [decode(k) for k in params[key]]
        else:
            params[key] = decode(params[key])
    map(inner, keys)
    return params


def gather_keys(model):
    ret = []
    for k, v in model._properties.iteritems():
        if v.__class__.__name__ == "KeyProperty":
            ret.append(k)
    return ret


def random_alnum(count):
    chars = string.letters + string.digits
    result = ''
    for i in range(count):
        result += random.choice(chars)
    return result
