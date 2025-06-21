from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.extensions import db

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    return jsonify(restaurant.to_dict(include_pizzas=True)), 200

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204