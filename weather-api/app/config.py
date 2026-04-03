import os  #Used to access environment variables
from dotenv import load_dotenv   #Loads variables from .env file

load_dotenv()  #Reads .env and makes variables accessible

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")