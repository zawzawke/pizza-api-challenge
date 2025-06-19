from flask import Blueprint, request, jsonify
from models.restaurant_pizza import RestaurantPizza
from models.restaurant import Restaurant
from models.pizza import Pizza
from server.config import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    new_entry = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(new_entry)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    return jsonify({
        "id": new_entry.id,
        "price": new_entry.price,
        "pizza_id": pizza_id,
        "restaurant_id": restaurant_id,
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201