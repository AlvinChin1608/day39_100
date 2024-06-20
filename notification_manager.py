import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("./vars/.env")

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

        # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
        # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(

            from_='whatsapp:+14155238886',
            body=message_body,
            to='whatsapp:+601111579619'
        )
        print(message.sid)
