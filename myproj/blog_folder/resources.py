import uuid
from substanced.folder import SequentialAutoNamingFolder
from substanced.interfaces import IFolder
from zope.interface import implementer
from substanced.content import content
from pyramid.httpexceptions import HTTPFound

@content(
   'Folder',
    icon='glyphicon glyphicon-folder-open',
    add_view='add_folder',
)
@implementer(IFolder)
class  BlogFolder(SequentialAutoNamingFolder):
    """ A folder that contains blog entries """
    def __init__(self):
        super().__init__()
        
    def add_success(self, appstruct):
        registry = self.request.registry
        blog_folder = registry.content.create('Blog Folder', **appstruct)
        self.context.add(None, blog_folder)
        return HTTPFound(self.request.sdiapi.mgmt_path(self.context, '@@contents'))

    '''def add(self, name, content):
        # Override the add method to customize the behavior of adding content to the folder
        # Your implementation here
        pass

    def remove(self, name):
        # Override the remove method to customize the behavior of removing content from the folder
        # Your implementation here
        pass

    def rename(self, old_name, new_name):
        # Override the rename method to customize the behavior of renaming content in the folder
        # Your implementation here
        pass

    def move(self, name, new_parent):
        # Override the move method to customize the behavior of moving content to a different folder
        # Your implementation here
        pass

    def copy(self, name, new_parent):
        # Override the copy method to customize the behavior of copying content to a different folder
        # Your implementation here
        pass

    def get(self, name, default=None):
        # Override the get method to customize the behavior of retrieving content from the folder
        # Your implementation here
        pass

    def keys(self):
        # Override the keys method to customize the behavior of retrieving the keys of the content in the folder
        # Your implementation here
        pass

    def values(self):
        # Override the values method to customize the behavior of retrieving the values of the content in the folder
        # Your implementation here
        pass

    def items(self):
        # Override the items method to customize the behavior of retrieving the items (key-value pairs) of the content in the folder
        # Your implementation here
        pass

    def __iter__(self):
        # Override the __iter__ method to customize the behavior of iterating over the content in the folder
        # Your implementation here
        pass

    def __len__(self):
        # Override the __len__ method to customize the behavior of getting the length of the folder (number of items)
        # Your implementation here
        pass
'''