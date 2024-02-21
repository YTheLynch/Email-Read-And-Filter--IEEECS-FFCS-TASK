from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail("client_secret.json")

query_params = {
    "newer_than": (2, "days")
}

messages = gmail.get_messages(query = construct_query(query_params))

for message in messages:
    print(message.sender)
    print(message.plain)