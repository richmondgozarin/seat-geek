from ferris import Controller, scaffold, messages, route_with
from app.models.account import Account
import json


class Accounts(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, messages.Messaging,)
        Model = Account

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete

    @route_with('/api/accounts', methods=['GET'])
    def api_list(self):
        self.context['data'] = Account.list_all()

    @route_with('/api/accounts', methods=['POST'])
    def api_post(self):
        Account.create(json.loads(self.request.body))
        return 200
