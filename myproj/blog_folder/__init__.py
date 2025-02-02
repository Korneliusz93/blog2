# in a module named blog.__init__

from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator()
    config.include('substanced')
    config.scan('blog_folder.resources')

def includeme(config):
    config.scan('.resources')
    config.scan('.views')