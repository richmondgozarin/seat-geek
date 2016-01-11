from google.appengine.api import users
from ferris import Controller, route_with


class Main(Controller):

    @route_with(template='/')
    def show(self):
        self.meta.view.template_name = 'angular/app-index.html'
        user = users.get_current_user()
        self.context['active_user'] = user.email()
        self.context['logout_url'] = users.create_logout_url('/')

    @route_with(template='/admin')
    def dashboard(self):
        self.meta.view.template_name = 'angular/admin.html'

    @route_with(template='/admin')
    def admin(self):
        self.meta.view.template_name = 'angular/admin-index.html'
        user = users.get_current_user()
        self.context['active_user'] = user.email()
        self.context['logout_url'] = users.create_logout_url('/')
