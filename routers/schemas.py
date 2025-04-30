from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    image_url: str
    creator: str

# Sample mock data for testing the API
mock_posts = [
    {
        "title": "Tokyo, Japan",
        "content": "Tokyo is the bustling capital of Japan, known for its ultramodern skyline and traditional temples. The city is a fascinating blend of old and new, where ancient shrines stand in the shadows of towering skyscrapers.\n\nWith its vibrant food scene, efficient public transportation, and unique pop culture, Tokyo offers visitors an unforgettable experience that stimulates all the senses.",
        "image_url": "tokyo.jpg",
        "creator": "travel_enthusiast"
    },
    {
        "title": "Rio de Janeiro, Brazil",
        "content": "Rio de Janeiro is famous for its stunning beaches, dramatic mountains, and lively carnival celebrations. The iconic Christ the Redeemer statue atop Corcovado mountain offers breathtaking views of the city and Guanabara Bay.\n\nThe city's vibrant culture is evident in its music, dance, and cuisine, making Rio a paradise for those seeking both natural beauty and cultural richness.",
        "image_url": "rio.jpg",
        "creator": "beach_lover"
    },
    {
        "title": "Marrakech, Morocco",
        "content": "Marrakech is a magical city in Morocco known for its historic medina, colorful souks, and stunning palaces. Visitors can get lost in the labyrinthine streets filled with vendors selling everything from spices to handcrafted goods.\n\nThe city's architecture features intricate tilework, peaceful courtyards, and beautiful gardens, all set against the backdrop of the Atlas Mountains, creating an atmosphere that feels like stepping into another world.",
        "image_url": "marrakech.jpg",
        "creator": "history_buff"
    }
]


class PostDisplay(BaseModel):
    id: int
    title: str
    content: str
    image_url: str
    creator: str
    created_at: datetime

    class Config:
        orm_mode = True