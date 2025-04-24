import requests
import os
from datetime import datetime

APPLICATION_ID = os.environ.get("APP_ID")
APPLICATION_KEY = os.environ.get("APP_KEY")

# connecting to nutritionx api.
NL_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

excercise_text = input("Give a description of the activity/excercise you participated in: ")

w_params = {
    'query': excercise_text,
    'age': 32,
    'weight_kg': 108,
    'height_cm': 182.88,
}

w_headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY,

}

workout_post = requests.post(url=NL_ENDPOINT, json=w_params, headers=w_headers)
results = workout_post.json()

# connecting to Sheety API

sheety_endpoint = 'https://api.sheety.co/9a5f2f38c579638928123fbfa4eab617/workoutsTracking/workouts'


date = datetime.now().strftime('%m/%d/%Y')
time = datetime.now().strftime('%H:%M:%S')

for excercise in results["exercises"]
    sheet_input = {
        'workout':{
            'date': date,
            'time': time,
            'excercise': excercise['name'],
            'duration': excercise['duration_min'],
            'calories': excercise['nf_calories',]

        }
    }

    sheet_response = 

