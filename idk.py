import requests
import json
# URL získaná z Teams webhooku
webhook_url = "https://ssinfis.webhook.office.com/webhookb2/138d042a-8952-407b-b941-9763db66acd5@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/88666a9fbdbb4aa6923ab4a338b3252b/c7a497c2-1179-4bbe-810d-af20971c91bb/V2OP1u6iMVXAbnv49YlNBPuxGWNc73fw_-GiCURzxmpv01"
# Text zprávy
message = {
   "text": "Ahoj, tohle je zpráva z Pythonu!"
}
# Odeslání POST požadavku
response = requests.post(
   url=webhook_url,
   data=json.dumps(message),
   headers={'Content-Type': 'application/json'}
)
# Kontrola odpovědi
if response.status_code == 200:
   print("Zpráva úspěšně odeslána.")
else:
   print(f"Chyba: {response.status_code}, {response.text}")