from twilio.rest import Client
from credentials import account_sid, auth_token, recv_number, twiml_url, trial_no


def sms(msg="URGENT! SOS BY VIA"):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_= trial_no,to= recv_number)


def dial():
    client = Client(account_sid, auth_token)
    client.calls.create(to=recv_number, from_= trial_no,url=twiml_url, method="GET")
