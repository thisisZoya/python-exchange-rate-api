from twilio.rest import Client
import os

def send_msg(text):
    account_sid = 'AC3409fcd77d3d71a184116c6385b0413b'
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG0584b2dc237016b162d5ff9c1742abca',
        body=text,
        to='+18777804236'  
    )

    print(message.sid)