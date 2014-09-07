#!/usr/bin/python  
   
 ## Author: Alexander Melikian  
 ##  
 ## copyright 2013, Alexander Melikian  
 ##  
 ## This script checks for unread Facebook messages and displays them  
 ##  
   
from facepy import GraphAPI  
   
def get_name_from_uid(author_id):  
    query_string = "SELECT name FROM user WHERE uid = " + str(author_id)  
    author = graph.fql(query_string)  
    if author['data']:  
        return author['data'][0]['name']  
    else:  
        return "Invalid ID"  
   
def print_recipients(recipients, message):  
    recipients.remove(message['snippet_author'])  
    for recipient in recipients:  
        print "  " + get_name_from_uid(recipient)  
   
def get_messages(message_list):  
    for message in message_list:  
        if message:  
	        print "FROM"  
        	print "  " + get_name_from_uid(message['snippet_author'])  
   
  	      	print "RECIPIENT(S)"  
		print print_recipients(message['recipients'], message)  
         
     	        print "BODY: " + message['snippet']  
        	print "-" * 40 + '\n'  
   
 # Initialize the Graph API with a valid access token  
oauth_access_token = 'your_access_token_goes_here_in_single_quotes'  
graph = GraphAPI(oauth_access_token)  
   
 # FQL: get all messages from inbox  
fql_get_messages = graph.fql(  
        'SELECT snippet, recipients, snippet_author, updated_time FROM thread WHERE folder_id = 1 and unread != 0')  
   
 # Get the data of the messages in a list  
message_list = fql_get_messages['data']  
   
 # print the messages 
if message_list:  
    get_messages(message_list)  
else:  
    print "Inbox is Empty"  
   
