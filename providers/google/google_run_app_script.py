"""
Shows basic usage of the Apps Script API.

"""
import json
from googleapiclient import errors
from googleapiclient.discovery import build

from providers.google.get_credentials import GoogleCredentials
from common.config import initialize_config

SCRIPT_ID = '1FJi_cMqS8i1g5tvDMZa7qC60NW0vWSDf4pIOeggLSt5eIwbuPuyjJrB2'


def run_app_script(credentials=None, script_id=SCRIPT_ID,
                   function_name="myFunction",
                   params=None):
    """Calls the Apps Script API.
    """
    # store = oauth_file.Storage('token2.json')
    # creds = store.get()
    # if not creds or creds.invalid:
    #     flow = client.flow_from_clientsecrets('client.json', SCOPES)
    #     creds = tools.run_flow(flow, store)

    if not credentials:
       credentials = GoogleCredentials().get_credential_local()
    service = build('script', 'v1', credentials=credentials)

    # Call the Apps Script API
    result = []
    try:
        # Create an execution request object.
        request = {"function": function_name, "parameters": params}
        response = service.scripts().run(body=request,
                scriptId=script_id).execute()

        # print("..................")

        if 'error' in response:
            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                                              trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns.
            result = response['response'].get('result', {})
            if not result:
                print('No result returned!')
            else:
                print("Result: ", result)

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print("ERROR", e.content)
        result = {'error': e.content}

    return result


if __name__ == '__main__':
    initialize_config()
    creds = GoogleCredentials().get_credential()
    params = ['https://docs.google.com/forms/d/1IwByAkcyEsGZmuNTZKCavfQ2GxAPvr4_20wC-wnOCa0/edit',
              False]
    results = run_app_script(creds, function_name='getQuizDetails',
                             params=params)
    print(json.dumps(results, indent=4))
