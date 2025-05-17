import datetime
import colander
import deform.widget
from persistent import Persistent
from substanced.property import PropertySheet
from substanced.content import content
import re
from substanced.schema import (
    Schema,
    NameSchemaNode
)

def context_is_a_blog_entry(context, request):
    return request.registry.content.istype(context, 'BlogEntry')

@content('Blog Entry', icon='glyphicon glyphicon-book', add_view='add_blog_entry')
class BlogEntry(Persistent):
    
    def __init__(self, title='', body='', image_filename=''):
        self.title = title
        self.body = body
        self.paragraph = self.produce_post_preview()
        self.author = ''
        self.tags = []
        self.comments = []
        self.date = datetime.datetime.now()  # Automatically set the current date and time
        self.image_filename = image_filename
        self.image_url = None

    def produce_post_preview(self):
        first_paragraph =  "".join(re.sub(r'<.+?>','', re.split(r'\n+', str(self.body).strip())[0]))
        if first_paragraph.isspace():
            return 'No summary available'
        first_paragraph_words = first_paragraph.split(' ')
        return first_paragraph.replace('&nbsp;', ' ') + '...' if len(first_paragraph_words) < 30 else " ".join(first_paragraph_words[:30]).replace('&nbsp;', ' ') + '...'

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
    image_filename = colander.SchemaNode(
        colander.String(),
        title='Image URL',
        missing='',
        widget=deform.widget.TextInputWidget()
    )

class BlogEntrySheet(PropertySheet):
    schema = BlogEntrySchema()