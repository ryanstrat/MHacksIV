#!/usr/bin/python

import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run
from oauth2client.client import AccessTokenCredentials

import base64
def getData():
# Path to the client_secret.json file downloaded from the Developer Console
	CLIENT_SECRET_FILE = 'client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
	OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

# Location of the credentials storage file
	STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
	flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
	http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
	credentials = AccessTokenCredentials('ya29.eABuoT89OVHq9BwAAADzLlFeFA5k8pw89ImxT57CGgeFVOZqSNSkOswEU-aApQ', 'my-user-agent/1.0')
	if credentials is None or credentials.invalid:
  		credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
	http = credentials.authorize(http)

# Build the Gmail service from discovery
	gmail_service = build('gmail', 'v1', http=http)

# Retrieve a page of threads
	messages = gmail_service.users().messages().list(userId='me',q='in:sent after:2014/09/01',maxResults=1).execute()

	messages = messages['messages']
	datas = []
	for message in messages[0:1]:
		id = message['id']
		data = gmail_service.users().messages().get(userId='me',id=id,format="full").execute()
		body = data['payload']['body']
		print data['snippet']
		datas.append(data['snippet']

	return datas
