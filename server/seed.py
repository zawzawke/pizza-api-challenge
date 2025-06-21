from server.app import create_app
from server.extensions import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()
    print("Creating tables...")
    db.create_all()

    print("Seeding data...")

    # Sample Restaurants
    r1 = Restaurant(name="Luigi's Pizzeria", address="123 Mushroom Lane")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Witch Avenue")

    # Sample Pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    # Commit initial data
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("🌱 Done seeding!")
