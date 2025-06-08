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
    #schema = BlogEntrySchema()  # You can define a schema for BlogEntry similar to the Document schema
    buttons = ('add',)

    def __init__(self, context, request):
        super().__init__(context, request)
        #schema = BlogEntrySchema()
        schema = BlogEntrySchema().bind(request=self.request)
        root = self.request.root  # Access the root folder
        files = [
            (name, name) for name, obj in root.items()
            if obj.__class__.__name__ == 'File'  # Filter for File objects
        ]
        schema['files'].widget.values = files
        self.schema = schema
        
    def add_success(self, appstruct):
        registry = self.request.registry
        blog_entry = registry.content.create('Blog Entry', **appstruct)
        # Add selected files to the blog entry
        root = self.request.root
        selected_files = appstruct.get('files', [])
        print(f"Selected files: {selected_files}")  # Debugging output
        files_to_add = set()
        for file_name in selected_files:
            file_obj = root.get(file_name)
            if file_obj: #and isinstance(file_obj, substanced.file.File):
                print(f"Adding file: {file_obj}")  # Debugging output
                files_to_add.add(file_obj)

        blog_entry.files.update(files_to_add)

        self.context.add_next(blog_entry)
        return HTTPFound(self.request.resource_url(blog_entry))
    