import datetime
import colander
import deform.widget
from persistent import Persistent
from substanced.property import PropertySheet
from substanced.content import content
from substanced.schema import (
    Schema,
    NameSchemaNode
)
from substanced.util import renamer
import hashlib
import secrets

def context_is_a_blog_entry(context, request):
    return request.registry.content.istype(context, 'BlogEntry')

@content('Blog Entry', icon='glyphicon glyphicon-book', add_view='add_blog_entry')
class BlogEntry(Persistent):
    
    def __init__(self, title='', body=''):
        self.title = title
        self.body = body
        self.date = datetime.datetime.now()  # Automatically set the current date and time

def get_hash_value():
    hash_value = secrets.token_hex(32)
    return hash_value

class BlogEntrySchema(Schema):

    title = colander.SchemaNode(
        colander.String()
    )
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
    )
    date = colander.SchemaNode(
        colander.DateTime(),
        widget=deform.widget.HiddenWidget(),
        missing=colander.drop
    )

class BlogEntrySheet(PropertySheet):
    schema = BlogEntrySchema()