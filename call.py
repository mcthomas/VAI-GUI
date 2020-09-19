from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+13345085372"
# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+919106514839"]
# URL location of TwiML instructions for how to handle the phone call
# Twilio API credentials
# Found at https://www.twilio.com/console
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("AAC3315d990c8acea7fe1714c4a4ee9cf61", "3e8fc6ea2a4adae5569fa10cbcd8587d")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
