
from pyramid.httpexceptions import HTTPFound
from pyramid.view import (
    view_config,
    view_defaults,
    )
from substanced.sdi import mgmt_view
from pyramid.httpexceptions import HTTPFound
from substanced.form import FormView
import uuid

from ..blog_folder.resources import BlogFolder

from .resources import MultimediaFileSchema, MultimediaFile

@mgmt_view(
    context=BlogFolder,
    name='add_file',
    tab_title='Add Multimedia File',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
)
class AddMultimediaFileView(FormView):
    schema = MultimediaFileSchema()
    title = 'Add Multimedia File'
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        multimedia_file = registry.content.create('Multimedia File')
        
        # Handle file data
        file_data = appstruct['file']
        multimedia_file.set_file_data(file_data)

        self.context.add_next(multimedia_file)
        return HTTPFound(self.request.sdiapi.mgmt_path(self.context, '@@contents'))