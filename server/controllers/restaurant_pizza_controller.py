from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.extensions import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        new_entry = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_entry)
        db.session.commit()

        restaurant = Restaurant.query.get(data['restaurant_id'])

        return jsonify({
            "id": new_entry.id,
            "pizza_id": new_entry.pizza_id,
            "restaurant_id": new_entry.restaurant_id,
            "price": new_entry.price,
            "restaurant": restaurant.to_dict() if restaurant else None
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
