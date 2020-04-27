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


class GoogleCredentails:
    credential = None

    def __init__(self):
        self.credential = None
        self.expiry = None
        pass

    def get_credential(self, token_file=None):
        """allow access using token file from cloud
        """
        cloud_provider['cloud_config_file'] = token_file or 'token2.pickle'
        token = get_config_file(cloud_provider)
        self.credential = pickle.loads(token)
        return self.credential

    def get_credential_from_token(self, token_id=None, access_token=None):
        """allow access using logged in user from UI
        """
        client_id = get_config("application_client_id")
        id_info = id_token.verify_oauth2_token(token_id, Request(), client_id)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        #creds = Credentials.from_authorized_user_info(idinfo)
        self.credential = Credentials(access_token, id_token=token_id)

        return self.credential, id_info

    def get_cred(self, token_file='token2.pickle', credential_file='client.json'):
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

        self.credential = creds
        return self.credential


if __name__ == '__main__':

    # creds = get_cred()
    # add_course()

    #creds = get_credential('token2.pickle')
    gc = GoogleCredentails()

    token_id = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY5ZDk3YjRjYWU5MGJjZDc2YWViMjAwMjZmNmI3NzBjYWMyMjE3ODMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODA3Njg2NTA0MTk4LWs5b2I1czRnNGt1bnVma3J0YjZtYjlzNnNyM2RrYXR1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODA3Njg2NTA0MTk4LWs5b2I1czRnNGt1bnVma3J0YjZtYjlzNnNyM2RrYXR1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAyOTE5Njg2OTIwNjYxNzU2NTU1IiwiZW1haWwiOiJmYXJydWtoNTAzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoibGowV0psNE84ZEdBRU1GU0RCbjR6USIsIm5hbWUiOiJGYXJydWtoIFNoYWh6YWQiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2dqeUlLMU13WGNRd1RvRm9lM3dkV0oxMDRRN1NLalF3X0tIcmR3N0E9czk2LWMiLCJnaXZlbl9uYW1lIjoiRmFycnVraCIsImZhbWlseV9uYW1lIjoiU2hhaHphZCIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNTg3ODQwNTkzLCJleHAiOjE1ODc4NDQxOTMsImp0aSI6ImY0MmE0ZDZkNWRjMTBjMjE0MGM5ZmJmYTRhY2I3YWM3MWMzOTZmZWYifQ.fDKjBjHimag1HUBA5B24JHQIR6UmywkbyDOj6mJ_mjGRwxKH8kCm3tb-IMy3B13BKb98z48_VbuCKXPS-Xdel9O2pV29qOg3jzcwAmO6_32IttzCKQheIOQ-zEWe0_URjZrKQWht99_Pk-XMM81g-q6V33u0_JNUvAvE6xqSAo8Z-vW6caatIuAVJ7AccxuyVxEHcRNYktaeyUanpt7jJ6lQTKQrS-URubWBrMsBD7FXD6pI34ArCtPXsEmtW3ckm1ercTpjBU3fhH0imAbDidco4kw3e3_SxeKZ-Iwm_frODfN3fl8bKZwkOzPS1AKMQb8ONglc1e9Uu3EFE1xEDA"
    access_token = "ya29.a0Ae4lvC06R0_f0FsZaMAvtHdNvcjWvSbXBPY6x_LPQug9l_8Y5N2gcQd5ODE5lubGkuzVMS3bN29DxQU4aDqDW4RHOWaKyUrumnrc8cGeXcf5E9_O3tQnA4x5s2xyHGKdPRRpyl086oL3decizSDDRsNW3_66h4Q8Dks"
    creds, info = gc.get_credential_from_token(token_id, access_token)
    print(creds.refresh_token, creds.client_id, creds.client_secret, creds.expired)
