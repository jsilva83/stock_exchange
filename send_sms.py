# Import external modules.
import twilio.rest as twi
import os


class TwilioSMS:

    def __init__(self):
        """
        Initialize the object and set the object attributes to send the SMS.
        """
        self.my_twilio_account_sid = os.environ.get('MY_TWILIO_ACCOUNT_SID')
        if self.my_twilio_account_sid is None:
            import api_keys
            self.my_twilio_account_sid = api_keys.MY_TWILIO_ACCOUNT_SID
        self.my_twilio_account_auth_token = os.environ.get('MY_TWILIO_ACCOUNT_AUTH_TOKEN')
        if self.my_twilio_account_auth_token is None:
            import api_keys
            self.my_twilio_account_auth_token = api_keys.MY_TWILIO_ACCOUNT_AUTH_TOKEN
        self.my_twilio_phone_number = os.environ.get('MY_TWILIO_PHONE_NUMBER')
        if self.my_twilio_phone_number is None:
            import api_keys
            self.my_twilio_phone_number = api_keys.MY_TWILIO_PHONE_NUMBER
        self.my_phone_number = os.environ.get('MY_PHONE_NUMBER')
        if self.my_phone_number is None:
            import api_keys
            self.my_phone_number = api_keys.MY_PHONE_NUMBER
        # Create the connection client.
        self.twilio_client = twi.Client(self.my_twilio_account_sid, self.my_twilio_account_auth_token)
        # What if the client returns an error?
        return

    def send_sms(self, in_message):
        """
        Sends an SMS message using the twilio service.
        :param in_message: (str) Message to send using SMS.
        :return:
        """
        twilio_message = self.twilio_client.messages.create(
            from_=self.my_twilio_phone_number,
            to=self.my_phone_number,
            body=in_message,
        )
        return
