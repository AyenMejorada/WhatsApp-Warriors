from twilio.rest import Client
from datetime import datetime

ACCOUNT_SID = 'ACc3352e66ad57fcdbf2cf3f2d68dac88a'
AUTH_TOKEN = '[AuthToken]'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_notification(user_number, event_details):
    try:
        message_content = (
            f"Dear User,\n\n"
            f"Your enrollment status: {event_details['status']}.\n"
            f"UIN: {event_details['uin']}.\n"
            f"Notification Time: {event_details['timestamp']}.\n\n"
            f"Thank you for using the National ID System."
        )

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_content,
            to=f'whatsapp:{user_number}'
        )

        print(f"Message sent successfully! SID: {message.sid}")

    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    user_number = '+639123456789'
    event_details = {
        'status': 'Completed',
        'uin': '1234-5678-9101',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    send_whatsapp_notification(user_number, event_details)