# pip install twilio


#API to using in twillio
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def incoming_message():
    message_body = request.form['Body']
    sender = request.form['From']
    response = process_message(message_body, sender)
    twiml = MessagingResponse()
    twiml.message(response)
    return str(twiml)


# -------------------------------
# Process message 

def process_message(message_body, sender):
    if message_body.lower() == 'hi':
        return 'Hello, how can I help you?'
    elif 'vacation' in message_body.lower():
        return 'Sure, we can help you plan your vacation! Where would you like to go?'
    else:
        return "I'm sorry, I didn't understand. How can I assist you?"


# --------------------------
# To send message
from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_message(to, body):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to}',
        body=body
    )
    return message.sid
