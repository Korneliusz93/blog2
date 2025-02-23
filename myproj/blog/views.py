# in a module named blog.views

from pyramid.httpexceptions import HTTPFound
from pyramid.view import (
    view_config,
    view_defaults,
    )
from substanced.sdi import mgmt_view
from pyramid.httpexceptions import HTTPFound
from substanced.form import FormView

from ..blog_folder.resources import BlogFolder

from .resources import BlogEntrySchema

@mgmt_view(
    context=BlogFolder,  # Use BlogFolder or adjust based on your content structure
    name='add_blog_entry',
    tab_title='Add Blog Entry',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
)
class AddBlogEntryView(FormView):
    title = 'Add Blog Entry'
    schema = BlogEntrySchema()  # You can define a schema for BlogEntry similar to the Document schema
    buttons = ('add',)
        
    def add_success(self, appstruct):
        registry = self.request.registry
        blog_entry = registry.content.create('Blog Entry', **appstruct)
        self.context.add_next(blog_entry)
        return HTTPFound(self.request.sdiapi.mgmt_path(self.context, '@@contents'))
    