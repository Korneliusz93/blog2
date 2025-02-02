# in a module named blog.__init__

from pyramid.config import Configurator
from .resources import BlogEntry, BlogEntrySheet

def main(global_config, **settings):
    config = Configurator()
    config.include('substanced')
    config.scan('blog.resources')
    config.scan('blog.views')
    
def includeme(config):
    """This function is called when the blog module is included."""
    config.add_propertysheet('Basic', BlogEntrySheet, BlogEntry)
    config.scan('.resources')
    config.scan('.views')
