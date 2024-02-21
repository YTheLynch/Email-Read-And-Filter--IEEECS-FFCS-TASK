import os.path
from time import strftime, gmtime, time
import base64
import email


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def numdaystosearchquerytime(n):
    starttime = gmtime(time() - n * 60 * 60 * 24)
    return strftime("%Y/%m/%d", starttime)

def search_messages(service, search_string = "", user_id = 'me'):
    try:
        search_id = service.users().messages().list(userId = user_id, q = search_string).execute()


        numresults = search_id['resultSizeEstimate']
        id_list = []
        if numresults > 0:
            message_ids = search_id['messages']
            for ids in message_ids:
                id_list.append(ids['id'])
            
            return id_list
        else:
            return []

    except HttpError as error:
        print(f"An error occurred: {error}")
    

def get_message(service, user_id, msg_id):
    try:
        message = service.users().messages().get(userId = user_id, id = msg_id, format = 'raw').execute()
        msg_raw = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
        msg_str = email.message_from_bytes(msg_raw)

        content_type = msg_str.get_content_maintype()

        if content_type == 'multipart':
            # part1 contains plain text, part2 is html text
            part1, part2 = msg_str.get_payload()
            return part1.get_payload()
        else:
            return msg_str.get_payload()

    except HttpError as error:
        print(f"An error occurred: {error}")


def get_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)

    except HttpError as error:
        print(f"An error occurred: {error}")

    return service
  




search_messages(get_service(), search_string = f"after:{numdaystosearchquerytime(7)}")