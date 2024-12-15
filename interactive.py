from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os

ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def handle_whatsapp_message(incoming_msg, sender_number):
    resp = MessagingResponse()
    msg = resp.message()

    if 'status' in incoming_msg.lower():
        msg.body("You asked about your Application Status. Checking now...")
        application_status = "Your application is under review. Please check again later."
        msg.body(application_status)

    elif 'uin' in incoming_msg.lower():
        msg.body("You asked to download your UIN card. Proceeding now...")
        msg.body("Click here to download your UIN card: [link_to_download_UIN_card]")

    else:
        msg.body("Welcome! Please reply with 'status' to check your application status or 'uin' to download your UIN card.")

    print(f"Message sent to {sender_number}: {msg.body}")
    return str(resp)

if __name__ == "__main__":
    incoming_msg = "status"
    sender_number = "+639123456789"
    response = handle_whatsapp_message(incoming_msg, sender_number)
    print(response)