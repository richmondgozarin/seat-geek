from ferris import Controller, scaffold
from app.models.ticket import Ticket


class Tickets(Controller):
    class Meta:
        prefixes = ('admin',)
        components = (scaffold.Scaffolding,)
        Model = Ticket

    admin_list = scaffold.list        #lists all posts
    admin_view = scaffold.view        #view a post
    admin_add = scaffold.add          #add a new post
    admin_edit = scaffold.edit        #edit a post
    admin_delete = scaffold.delete    #delete a post
