
from pyramid.config import Configurator
from deform.interfaces import FileUploadTempStore
from .resources import MultimediaFile

def main(global_config, **settings):
    config = Configurator()
    config.include('substanced')
    config.scan('multimedia_file.resources')
    config.scan('multimedia_file.views')

def includeme(config):
    config.scan('.resources')
    config.scan('.views')