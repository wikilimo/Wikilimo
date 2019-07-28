### This directory contains the source code for the Wikilimo platform's offline functionality.

## User Guide

1. All required python libraries can be installed by running `pip install -r requirements.txt`.

2. Run [this](https://github.com/lazyoracle/OpenCIPlatform/blob/master/Wikilimo_offline/Wikilimo_SMS_weather_alerts.py) Python script for a demo of Wikilimo's SMS service for sending Weather Alerts:
`python Wikilimo_SMS.py <recipient phone numbers>`
###### *(Eg, python Wikilimo_SMS.py +1xxxxxxxxxx +1xxxxxxxxxx ..)*

We can additionally integrate the following web APIs:
 - **[Agro API v1.0](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/agro-api-usage-examples.html)**, providing soil data and satellite imagery search and download
 - **[Air Pollution API v3.0](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/air-pollution-api-usage-examples.html)**, providing data about CO, O3, NO2 and SO2
 - **[UV Index API v3.0](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/uv-api-usage-examples.html)**, providing data about Ultraviolet exposition
 - **[Stations API v3.0](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/stations-api-usage-examples.html)**, allowing to create and manage meteostation and publish local weather measurements
 - **[Weather Alerts API v3.0](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/alerts-api-usage-examples.html)**, allowing to set triggers on weather conditions and areas and poll for spawned alerts
 - **[Image tiles](https://pyowm.readthedocs.io/en/latest/usage-examples-v2/map-tiles-client-examples.html)** for several map layers provided by OWM
