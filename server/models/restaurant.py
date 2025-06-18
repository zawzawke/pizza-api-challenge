from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String
from server.config import db
from .restaurant_pizza import RestaurantPizza

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza', 
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

