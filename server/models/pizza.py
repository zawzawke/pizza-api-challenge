from sqlalchemy import Column, Integer, String
from server.config import db

class Pizza(deb.model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='pizza'
    )