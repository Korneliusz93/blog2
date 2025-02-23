from pyramid.renderers import get_renderer
from pyramid.view import view_config
from ..resources import Document
from pyramid.response import Response
from ..blog.resources import BlogEntry
import pytz

#
#   Default "retail" view
#
@view_config(
    renderer='templates/splash.pt',
    )
def splash_view(request):
    manage_prefix = request.registry.settings.get('substanced.manage_prefix',
                                                  '/manage')
    return {'manage_prefix': manage_prefix}

#
#   "Retail" view for documents.
#
@view_config(
    context=Document,
    renderer='templates/document.pt',
    )
def document_view(context, request):
    return {'title': context.title,
            'body': context.body,
            'master': get_renderer('templates/master.pt').implementation(),
           }

@view_config(content_type='Root', renderer='templates/welcome_screen.pt')
def welcome_screen(context, request):
    return {}

@view_config(context=BlogEntry, renderer='templates/blog_entry.pt')
def hello_world_of_blog_entry(context, request):
    return {'title': context.title, 'body': context.body, 'image_url':context.image_url, 'date': context.date.strftime('%Y-%m-%d %H:%M')}

@view_config(route_name='blog', renderer='templates/blog_list.pt')
def blog_list_view(request):
    root = request.root
    blog_entries = []

    # Assuming BlogEntry items are stored in a folder named 'blog'
    blog_folder = root.get('blog', None)
    if blog_folder:
        for name, resource in blog_folder.items():
            if isinstance(resource, BlogEntry):
                blog_entries.append(resource)
    
    # Convert all dates to offset-aware (UTC)
    for entry in blog_entries:
        if entry.date.tzinfo is None:
            entry.date = entry.date.replace(tzinfo=pytz.UTC)

    # Sort blog entries chronologically by a hypothetical 'created' attribute
    blog_entries.sort(key=lambda entry: entry.date, reverse=True)

    # Pagination logic
    try:
        page = int(request.params.get('page', 1))
    except (TypeError, ValueError):
        page = 1

    try:
        page_size = int(request.params.get('page_size', 10))
    except (TypeError, ValueError):
        page_size = 10
    
    start = (page - 1) * page_size
    end = start + page_size
    
    paginated_entries = blog_entries[start:end]
    total_entries = len(blog_entries)

    return {
        'blog_entries': paginated_entries,
        'page': page,
        'page_size': page_size,
        'total_entries': total_entries,
    }