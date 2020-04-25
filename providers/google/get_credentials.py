import pickle
import os


# need to install these using pip install --upgrade
# google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.oauth2 import id_token
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from providers.cloud_handler import get_config_file
from api.config import cloud_provider, get_config

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses',
          'https://www.googleapis.com/auth/classroom.coursework.me',
          'https://www.googleapis.com/auth/classroom.coursework.students',
          'https://www.googleapis.com/auth/classroom.rosters',
          'https://www.googleapis.com/auth/classroom.profile.emails',
          'https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/forms',
          'https://www.googleapis.com/auth/drive']

# https://www.googleapis.com/auth/classroom.topics
# https://www.googleapis.com/auth/classroom.push-notifications
# https://www.googleapis.com/auth/classroom.announcements


def get_credential(token_file=None):
    """allow access using token file from cloud
    """
    cloud_provider['cloud_config_file'] = token_file or 'token2.pickle'
    token = get_config_file(cloud_provider)
    return pickle.loads(token)


def get_credential_from_token(token_id=None, access_token=None):
    """allow access using logged in user from UI
    """
    client_id = get_config("application_client_id")
    id_info = id_token.verify_oauth2_token(token_id, Request(), client_id)
    if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')
    #creds = Credentials.from_authorized_user_info(idinfo)
    credential = Credentials(access_token, id_token=token_id)

    return credential, id_info


def get_cred(token_file='token2.pickle', credential_file='client.json'):
    """allow access using local token file or client json file
    """
    creds = None
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    #print(creds.valid, creds.expired)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        #os.environ['OAUTHLIB_STRICT_TOKEN_TYPE'] = "1"
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return creds