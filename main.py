import json
import requests
import uvicorn
from fastapi import FastAPI
from settings import settings

AIRTABLE_BASE_ID = settings.AIRTABLE_BASE_ID
AIRTABLE_TABLE_NAME = settings.AT_MANUFACTURER_TABLE
AIRTABLE_API_KEY = settings.AIRTABLE_API_KEY

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.post("/api")
def airtable_trigger():
    try:
        endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
        print(endpoint)
        headers= {
                "Authorization": f"Bearer {AIRTABLE_API_KEY}",
                "Content-Type":"application/json"
                }
        print(headers)
        #record_dict = {'fields': {"recipient": (', ').join([str(email) for email in RECIPIENT]), "message_id": response['MessageId'], "uuid": uuid, "username": username, "first_name": first_name, "last_name": last_name, "email_content": bodyContent, "send_date": str(datetime.now()), "sender": SENDER, "subject": subject, "template": template}}
        #print(record_dict)
        #data = json.dumps(record_dict)
        #print(data)
        try:
            #r = requests.post(endpoint, data=data, headers=headers)
            r = requests.get(endpoint, headers=headers)
            print(r.status_code, r.json())

            # Parse response
            data = r.json()
            records = data['records']
            print(records)
        except Exception as e:
            print(repr(e))
    except Exception as e:
        print(repr(e))
    return {'records': records}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
