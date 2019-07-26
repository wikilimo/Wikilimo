"""
Send SMS feature for Wikilimo Platform
@author: roshni-b
"""

import africastalking
import argparse


def send_SMS(text, recipients):
    # Initializing the Africa's Talking SMS service
    sms = africastalking.SMS
    response = sms.send(text, recipients)
    return (response)


def main():
    # Initializing SDK
    username = "roshnib"
    api_key = "a8bc7ce85d25386799d345f0c82a144811f86e4d2b13dc89efc20f9f1b6454e4"
    africastalking.initialize(username, api_key)

    # Defining arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='a text message to be sent as SMS')
    parser.add_argument('recipients', nargs='*', help='phone number(s) of recipient(s)')
    args = parser.parse_args()
    text = args.text
    recipients = args.recipients

    # Send SMS(s)
    print(send_SMS(text, recipients))


if __name__ == "__main__":
    main()