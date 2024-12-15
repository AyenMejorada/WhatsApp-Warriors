# WhatsApp Warriors
 WhatsApp-Based Notification System for MOSIP

## Overview
This Python script shows how to send WhatsApp notifications for user enrollment status updates using Twilio's API. It is a prototype built to show how the National ID system can notify users in real time.

## Prerequisites
- A **paid Twilio account** (required for full functionality).
- Python 3.x installed on your machine.
- The `twilio` Python package. To install it, run:

  pip install twilio

## Setup Instructions
1. **Twilio Account**: 
   - Create a Twilio account if you don’t have one.
   - Replace the placeholder values in the script (`'your_account_sid'` and `'your_auth_token'`) with your actual Twilio account SID and authentication token. You can find these in your Twilio console.

2. **WhatsApp Sandbox Setup**: 
   - Follow the steps in Twilio’s [WhatsApp Quickstart Guide](https://www.twilio.com/docs/whatsapp/quickstart/python) to enable WhatsApp messaging through their sandbox environment.

3. **Run the Script**:
   - Once your Twilio account is set up and the script is configured with your credentials, run the script with:

     ```bash
     python send_notification.py
     ```

4. **Important Note**: 
   - Ensure you replace all placeholder values in the script (such as `'your_account_sid'` and `'your_auth_token'`) with actual values from your Twilio account. These placeholders will not work and the script will fail if left unchanged.

## How It Works
The script sends a WhatsApp notification to a user, providing their enrollment status, Unique Identification Number (UIN), and the time the message was sent. This is done using Twilio’s API.

## Limitations
- This script uses Twilio's sandbox for testing, which means it will only work with a **paid Twilio account**. Without a paid account, it will be limited to sending messages to a predefined set of numbers and cannot fully simulate real-world usage.
- The script is a prototype and isn't connected to the MOSIP system.

## Future Enhancements
- We aim to integrate the system directly with the MOSIP platform, replacing the Twilio sandbox with a production environment. This will improve the system’s reliability and performance.
- Custom notification templates will be developed to make the user experience more streamlined and aligned with the actual system.
- We plan to add multi-language support, allowing users from different regions to access the system more easily."# WhatsApp-Warriors-MOSIP-Hackathon" 
