# Weather Forecast

import random

def predict_weather():
    sunshine = random.choice([True, False]) # Changed from strings to Booleans

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")


predict_weather()