from ferris import Controller, scaffold, messages, route_with
from app.models.ticket import Ticket


class Tickets(Controller):
    class Meta:
        prefixes = ('admin', 'api',)
        components = (scaffold.Scaffolding, messages.Messaging,)
        Model = Ticket

    admin_list = scaffold.list        #lists all posts
    admin_view = scaffold.view        #view a post
    admin_add = scaffold.add          #add a new post
    admin_edit = scaffold.edit        #edit a post
    admin_delete = scaffold.delete    #delete a post

    @route_with('/api/tickets', methods=['GET'])
    def api_list(self):
        self.context['data'] = Ticket.list_all()
