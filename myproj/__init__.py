from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.view import view_config


from substanced.db import root_factory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=root_factory)
    
    config.add_static_view('static', 'myproj:retail/static', cache_max_age=3600)
    
    config.include('substanced')
    config.include('.resources')
    config.include('.blog')
    config.include('.retail')
    config.include('.blog_folder')
    config.add_route('blog', '/blog')  # Add route for the blog page
    config.scan()
    return config.make_wsgi_app()
