from twilio.rest import Client
twilio_account_sid="**********"
twilio_auth_token="**********"

client = Client(twilio_account_sid,twilio_auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number=['whatsapp:+918469991090']
for x in to_whatsapp_number:
    client.messages.create(body="hey",
                           from_=from_whatsapp_number,
                           to=x)
