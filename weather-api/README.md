This is a RESTful Weather API built using FastAPI that provides real-time weather information for any city using the OpenWeatherMap API.

The project is designed with a clean and modular architecture, making it scalable, maintainable, and easy to extend.

Features
Get real-time weather data by city
Fast and efficient API using FastAPI
Secure API key management using environment variables
Modular project structure (routes, services, config)
Automatic API documentation (Swagger UI)
Basic error handling for invalid inputs.

Backend: Python, FastAPI
API Integration: OpenWeatherMap API
Tools: Uvicorn, Postman
Environment Management: python-dotenv

Get Weather by City:
GET /weather/{city}

Example:
/weather/Bangalore
Sample Response:
{
  "city": "Bangalore",
  "temperature": 28,
  "weather": "clear sky"
}

API Documentation:
FastAPI provides built-in interactive documentation:

Swagger UI:
http://127.0.0.1:8000/docs

Error Handling:
Returns error message for invalid city names.
Handles external API failures.

Security:
API keys are stored securely using .env files
Sensitive data is not exposed in the codebase