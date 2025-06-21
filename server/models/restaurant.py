from sqlalchemy import Column, Integer, String
from server.extensions import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

    def to_dict(self, include_pizzas=False):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

        if include_pizzas:
            data["pizzas"] = [
                {
                    "id": rp.pizza.id,
                    "name": rp.pizza.name,
                    "ingredients": rp.pizza.ingredients
                } for rp in self.restaurant_pizzas
            ]

        return data
