from googleapiclient.http import MediaIoBaseUpload
import mimetypes

def load_file(service, buffer, file_name, destination_folder_id, destination_files):
    """Uploads to Drive, deciding between Create or Update."""
    buffer.seek(0)
    
    mime_type = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
    media = MediaIoBaseUpload(buffer, mimetype=mime_type, resumable=True)

    if file_name in destination_files:
        file_id = destination_files[file_name]['id']
        service.files().update(
            fileId=file_id, 
            media_body=media,
            supportsAllDrives=True
        ).execute()
    else:
        body = {'name': file_name, 'parents': [destination_folder_id]}
        service.files().create(
            body=body, 
            media_body=media,
            supportsAllDrives=True
        ).execute()