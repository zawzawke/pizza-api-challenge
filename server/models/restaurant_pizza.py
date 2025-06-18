from sqlalchemy import Column, Integer, ForeignKey
from server.config import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.model):
    __tablename__ = 'restaurant_pizzas'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)

    @validates('price')
    def validate_price(self, key, price):
        if not(1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return price