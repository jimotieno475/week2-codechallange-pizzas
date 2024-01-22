from models import  Restaurant, Pizza, RestaurantPizza
from app import db,app

with app.app_context():
    #Delete the existing data
    print('Deleting existing data...')
    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    # Create Restaurants
    restaurant1 = Restaurant(name='Pizza Place 1', address='123 Main St')
    restaurant2 = Restaurant(name='Italian Bistro', address='456 Oak St')

    # Create Pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato Sauce, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato Sauce, Mozzarella, Pepperoni')

    # Add Pizzas to Restaurants
    restaurant1.pizzas.append(pizza1)
    restaurant1.pizzas.append(pizza2)

    restaurant2.pizzas.append(pizza2)

    # Create Restaurant Pizzas
    restaurant_pizza1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    restaurant_pizza2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=restaurant1.id)
    restaurant_pizza3 = RestaurantPizza(price=15, pizza_id=pizza2.id, restaurant_id=restaurant2.id)

    # Add objects to the session and commit to the database
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()

# if __name__ == "__main__":
#     a()
