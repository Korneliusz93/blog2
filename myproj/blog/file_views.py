from pyramid.response import FileResponse
from pyramid.view import view_config
from substanced.file import File

@view_config(context=File, name='download', permission='view')
def download_file_view(context, request):
    print(f"Download view called for file: {context.__name__}")
    file_path = context.blob.committed()  # Assuming the file is stored as a blob
    print(f"File path: {file_path}")
    response = FileResponse(file_path, request=request)
    response.headers['Content-Disposition'] = f'attachment; filename="{context.__name__}"'
    return response