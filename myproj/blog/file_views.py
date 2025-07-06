from pyramid.response import FileResponse
from pyramid.view import view_config
from substanced.file import File
from pyramid.security import Everyone, Allow
from persistent import Persistent

@view_config(context=File, name='view', permission='view')
def view_file(context, request):
    print(f"Download view called for file: {context.__name__}")
    file_path = context.blob.committed()  # Assuming the file is stored as a blob
    print(f"File path: {file_path}")
    response = FileResponse(file_path, request=request)
    response.headers['Content-Disposition'] = f'attachment; filename="{context.__name__}"'
    return response

# In your ACL for File objects:
class File(Persistent):
    __acl__ = [
        (Allow, Everyone, 'view'),  # Allow everyone to view files
    ]