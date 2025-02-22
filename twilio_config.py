import os
from twilio.rest import Client
import config
# Your Account SID and Auth Token from twilio.com/console

client = Client(config.account_sid,config.auth_token)

ngrok_url = "https://0f27-2405-201-2004-3089-6434-53e2-fbd5-34ba.ngrok-free.app"  # Replace with your ngrok URL
webhook_url = f"{ngrok_url}/incoming-call"

try:
    # 1. Retrieve the desired phone number (example: the first voice-enabled number)
    numbers = client.incoming_phone_numbers.list(limit=100)  # Increased limit to ensure all numbers are retrieved

    voice_numbers = [number for number in numbers if number.capabilities.get("voice")]  # Filter voice-enabled numbers

    for voice_number in voice_numbers:
            phone_number = voice_number.phone_number
            print(f"Found phone number: {phone_number}")

            # 2. Update the phone number's webhook URL
            try:
                number = client.incoming_phone_numbers(phone_number).update(
                    voice_url=webhook_url
                )
                print(f"Updated phone number {phone_number} to use webhook URL: {webhook_url}")
            except Exception as e:
                print(f"Error updating phone number: {e}")

    else:
        print("No voice-enabled phone numbers found in your Twilio account.")

except Exception as e:
    print(f"Error retrieving phone numbers: {e}")

print("Configuration complete.")