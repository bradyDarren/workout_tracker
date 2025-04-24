import requests
import os

APPLICATION_ID = os.environ.get("APP_ID")
APPLICATION_KEY = os.environ.get("APP_KEY")

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

workout_post = requests.post(url=NL_ENDPOINT, params=w_params, headers=w_headers)
results = workout_post.json()
print(results)
