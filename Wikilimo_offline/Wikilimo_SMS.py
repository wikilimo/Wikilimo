"""
Send SMS with weather alerts, feature for the Wikilimo Platform
@author: roshni-b
"""

import africastalking
import argparse
import pyowm
import export_report
import locations


def get_present_weather_info(owm, latitude, longitude, location):
    """
      Query for pulling present weather information using the Open Weather Map API
      Args:
        owm (str): OWM API Key
        latitude (float): location info required for API call
        longitude (float): location info required for API call
        location (str): user input
      Returns:
        present_weather (str): Current weather conditions - temp, min temp, max temp, humidity, status
    """
    observation = owm.weather_at_coords(latitude, longitude)
    w = observation.get_weather()
    status = str(w.get_status())
    humidity = str(w.get_humidity())
    temp = str(w.get_temperature('celsius')['temp'])
    maxtemp = str(w.get_temperature('celsius')['temp_max'])
    mintemp = str(w.get_temperature('celsius')['temp_min'])
    present_weather = "Currently the temperature in " \
                      + location + " is: " + temp \
                      + "C; Maximum temperature is: " + maxtemp \
                      + "C; Minimum temperature is: " + mintemp \
                      + "C; Humidity is: " + humidity \
                      + "%. Overall status is: " + status+"."

    return present_weather


def get_forecast_weather_info(owm, latitude, longitude, date_format, location):
    """
      Query for pulling 3 hours weather forecast for the next 5 days from the Open Weather Map API
      Args:
        owm (str): OWM API Key
        latitude (float): location info required for API call
        longitude (float): location info required for API call
        date_format: ISO date-time formatting
        location (str): user input
      Returns:
        forecast_weather (str): Forecasted weather status for 40 timestamps
    """
    fc = owm.three_hours_forecast_at_coords(latitude, longitude)
    f = fc.get_forecast()
    forecast_weather = []
    for weather in f:
        forecast_weather += (weather.get_reference_time(date_format), weather.get_status())
    forecast_message = "The forecast for the next 5 days in "+location+" is: "
    forecast_weather = forecast_message + str(forecast_weather)
    return forecast_weather


def generate_sms(present_weather_info, forecast_weather_info, location):
    """
    Creates the message body for the SMS
      Args:
        present_weather_info (str): returned by get_present_weather_info()
        forecast_weather_info (str): returned by get_forecast_weather_info()
        location (str): user input
      Returns:
        sms_text_short (str): SMS body for a short weather update
        sms_text_long (str): SMS body for a detailed weather update with forecast info
    """
    welcome_text = "Hello from Wikilimo!\n\n"
    weather_update_text = "Here's a weather update for " + location + ":\n"
    sms_text_long = welcome_text + weather_update_text + present_weather_info + forecast_weather_info
    sms_text_short = welcome_text + weather_update_text + present_weather_info
    return sms_text_short, sms_text_long


def send_sms(text, recipients):
    """
    Sends the SMS to the recipient(s) using the Africa's Talking API
      Args:
        text (str): message body returned by generate_sms()
        recipients (str): Recipient's phone number(s) entered by user
      Returns:
        response (dict): JSON response from Africa's Talking with message delivery status code
    """
    # Initializing the Africa's Talking SMS service
    sms = africastalking.SMS
    response = sms.send(text, recipients)
    return response


def main():
    # Initializing SDKs for Africas Talking and Open Weather Map
    username = ""  # Account username
    api_key_at = ""  # Africa's Talking API Key
    api_key_owm = ""  # OWM Api Key
    africastalking.initialize(username, api_key_at)
    owm = pyowm.OWM(api_key_owm)

    date_format = 'iso'

    # Defining input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('location', help='City/Village name or nearest landmark')
    parser.add_argument('recipients', nargs='*', help='phone number(s) of recipient(s)')
    args = parser.parse_args()
    location = args.location
    recipients = args.recipients

    # Build functionality to set latest reported contact as sms recipient (currently user input)
    # recipient = str(export_report.get_latest_contact())

    latitude, longitude = locations.get_coords(location)

    present_weather_info = get_present_weather_info(owm, latitude, longitude, location)
    forecast_weather_info = get_forecast_weather_info(owm, latitude, longitude, date_format, location)
    short_text, long_text = (generate_sms(present_weather_info, forecast_weather_info, location))
    pest_report = "Hello from Wikilimo! \nA pest '" + \
                  str(export_report.get_latest_pest(export_report.sheet)) +\
                  "' has been recently reported nearby. Please take the necessary precautions."

    send_sms(short_text, recipients)
    send_sms(long_text, recipients)
    send_sms(pest_report, recipients)


if __name__ == "__main__":
    main()
