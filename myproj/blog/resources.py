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

def context_is_a_blog_entry(context, request):
    return request.registry.content.istype(context, 'BlogEntry')

@content('Blog Entry', icon='glyphicon glyphicon-book', add_view='add_blog_entry')
class BlogEntry(Persistent):
    
    def __init__(self, title='', body='', image_url=''):
        self.title = title
        self.body = body
        self.date = datetime.datetime.now()  # Automatically set the current date and time
        self.image_url = image_url

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
    image_url = colander.SchemaNode(
        colander.String(),
        title='Image URL',
        missing='',
        widget=deform.widget.TextInputWidget()
    )

class BlogEntrySheet(PropertySheet):
    schema = BlogEntrySchema()