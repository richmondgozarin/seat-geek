from ferris import scaffold, messages, Controller
from app.models.purchase import Purchase


class Purchases(Controller):
    class Meta:
        prefixes = ('api', 'admin')
        components = (scaffold.Scaffolding, messages.Messaging,)
        Model = Purchase

    admin_list = scaffold.list
    admin_view = scaffold.view
    admin_add = scaffold.add
    admin_edit = scaffold.edit
    admin_delete = scaffold.delete
