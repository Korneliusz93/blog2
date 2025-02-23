from io import BytesIO
import colander
import deform.widget
from persistent import Persistent
from substanced.property import PropertySheet
from substanced.content import content
from substanced.schema import (
    Schema,
    NameSchemaNode
)
from substanced.file import File
from substanced.interfaces import IFile
from zope.interface import implementer
from deform.interfaces import FileUploadTempStore
from ..memory_tmp_store import MemoryTmpStore


@content(
    'Multimedia File',
    icon='glyphicon glyphicon-film',
    add_view='add_file'
)
@implementer(IFile)
class MultimediaFile(File):
    def __init__(self, title='', description='', file=None):
        super().__init__()
        self.title = title
        self.description = description
        self.file = file

    def set_file_data(self, file_data):
        if file_data:
            input_file = file_data['fp']
            self.file = input_file.read()
            self.filename = file_data['filename']

class MultimediaFileSchema(Schema):
    # Define the schema without the 'name' field
    title = colander.SchemaNode(
        colander.String(),
        title='Title'
    )
    description = colander.SchemaNode(
        colander.String(),
        title='Description',
        missing=''
    )
    file = colander.SchemaNode(
        deform.FileData(),
        widget=deform.widget.FileUploadWidget(tmpstore = MemoryTmpStore())
    )
