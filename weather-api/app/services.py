# app/services.py
import requests  #requests helps to interact with APIs   
from app.config import API_KEY, BASE_URL  #reusing variables from config

def get_weather(city: str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "City not found"}  #Error Handling

    data = response.json()  #Helps to convert raw data from the api to list or dictionary in this case its dictionary

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }
    #returns only the specified data from the response