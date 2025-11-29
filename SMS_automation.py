from twilio.rest import Client

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

# Your Twilio phone number
TWILIO_PHONE_NUMBER = "+919024556032

# Recipients list (Your number + Friend's number)
RECIPIENTS = [
    "‪+919024559424‬",    # Your number
    "‪+917891079811‬",    # Friend's number
]

MESSAGE_TEXT = "Hello! This is an automated SMS sent using Python "

# FUNCTION TO SEND SMS_______________

def send_sms(message: str, to_number: str):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )

        print(f"SMS sent to {to_number} | SID: {sms.sid}")
    except Exception as e:
        print(f"Failed to send SMS to {to_number}: {e}")

# MAIN AUTOMATION LOGIC
if _name_ == "_main_":
    print(" Starting SMS automation...")

    for number in RECIPIENTS:
        send_sms(MESSAGE_TEXT, number)

    print(" All messages processed.")
