import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Manages authentication and returns the Google Drive service."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    path_credentials = os.path.join(base_path, 'credentials.json')
    path_token = os.path.join(base_path, 'token.json')

    creds = Credentials.from_authorized_user_file(path_token, SCOPES) if os.path.exists(path_token) else None
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = InstalledAppFlow.from_client_secrets_file(path_credentials, SCOPES).run_local_server(port=0)
        
        with open(path_token, 'w') as token:
            token.write(creds.to_json())
            
    return build('drive', 'v3', credentials=creds)

def list_files(service, folder_id):
    """Returns a dictionary {name: info} handling Google Drive pagination."""
    files_dict = {}
    query = f"'{folder_id}' in parents and trashed=false"
    page_token = None
    
    while True:
        response = service.files().list(
            q=query, 
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)",
            pageToken=page_token
        ).execute()
        
        for f in response.get('files', []):
            files_dict[f['name']] = f
            
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
            
    return files_dict
