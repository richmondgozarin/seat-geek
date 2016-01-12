from ferris.core import routing, plugins
from ferris.controllers.download import Download

# Routes all App handlers
routing.auto_route()
routing.route_controller(Download)
# Default root route
routing.redirect('/', to='/main')


# Plugins
#plugins.enable('settings')
#plugins.enable('oauth_manager')
plugins.enable('angular')
