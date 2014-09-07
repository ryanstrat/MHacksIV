from facepy import GraphAPI
client  = GraphAPI('CAACEdEose0cBAMRMJHGh7TPzi5h3MX35QZCRq7NSQbC0RHwo2jaRGmCLxAms4mluKpeyZC1LwPI6VUy83tvx2OdZCgJwE0ju2lT9hRPxJnw5HZAQYUoIEb3PsaoV8MSWPs8aGrvingMosqVatogsK7wtVVeuY1qFgVQYAtjVN34PKyyNxuQyQ2Pm5bcNGrJ9qUaftJSs4yaEUG7KqXDk')
user = client.get('me')
user_id = user['id']
messages = client.get('me/inbox')
threads  = messages['data']
message_bodies=[]
for thread in threads:
	try:
		messages  = thread['comments']['data']
		for message in messages:
			person_from = message['from']['id']
			body = message['message']
			if (person_from ==user_id):
				message_boddies.append(body)
	except:
		pass
