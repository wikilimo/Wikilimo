"""
USSD service built using Africa's Talking for querying current weather info, weather forecasts and pest infestation alerts for the Wikilimo platform
@author: roshni-b
"""

import os
from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/', methods = ['POST', 'GET'])

def ussd():
    global response
    session_id = request.values.get("sessionId", None)
    servicecode =  request.values.get("serviceCode", None) # '*384*1507#'
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", None)

    if text == "":
        response = "CON What would you like to check?\n"
        response += "1. Current weather status\n"
        response += "2. Weather forecast\n"
        response += "3. Pest infestations\n"
    elif text == "1":
        response = "END The weather in your location is: Sunny"
    elif text == "2":
        response = "END The weather forecast for the next 2 days is: Sunny/Partly Cloudy"
    elif text == "3":
        response = "END No pest infestations have been reported lately."
    else:
        response = "END Invalid choice"

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))