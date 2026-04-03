# app/routes.py
from fastapi import APIRouter
from app.services import get_weather

router = APIRouter()

@router.get("/weather/{city}")
def fetch_weather(city: str):
    return get_weather(city)