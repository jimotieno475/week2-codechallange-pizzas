import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request, make_response, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db,Pizza,Restaurant,RestaurantPizza
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api=Api(app)

class Restaurants(Resource):
    def get(self):
        restaurants=[r.to_dict() for r in Restaurant.query.all()]
        return make_response(jsonify(restaurants),200) 
    
class RestaurantsById(Resource):
    def get(self, id):
        try:
            # Fetch the Restaurant by id
            restaurant = Restaurant.query.get(id)

            if restaurant is None:
                # If the Restaurant does not exist, return an error
                return make_response(jsonify({'error': 'Restaurant not found'}), 404)

            # Fetch the pizzas associated with the restaurant
            pizzas = Pizza.query.join(RestaurantPizza).filter_by(restaurant_id=id).all()

            # Construct the response JSON
            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas]
            }

            return make_response(jsonify(restaurant_data), 200)

        except Exception as e:
            # Handle other exceptions as needed
            return make_response(jsonify({'error': 'An error occurred'}), 500)
    
    def delete(self,id):
        restaurant= Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()

        return make_response('',204)

class Pizzas(Resource):
    def get (self):
        pizzas=[p.to_dict()for p in Pizza.query.all()]
        return make_response(jsonify(pizzas),200)


class RestaurantPizzas(Resource):
    def post(self):
        try:
            data = request.get_json()

            # Check if the required fields are present
            if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
                raise ValueError('Missing required fields')

            # Fetch the associated Pizza and Restaurant
            pizza = Pizza.query.get(data['pizza_id'])
            restaurant = Restaurant.query.get(data['restaurant_id'])

            if pizza is None or restaurant is None:
                raise ValueError('Invalid pizza_id or restaurant_id')

            # Create a new RestaurantPizza
            new_rest_pizza = RestaurantPizza(
                price=data['price'],
                pizza_id=data['pizza_id'],
                restaurant_id=data['restaurant_id']
            )

            db.session.add(new_rest_pizza)
            db.session.commit()

            # Respond with the data related to the Pizza
            return make_response(jsonify(pizza.to_dict()), 201)

        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 400)
        except Exception as e:
            # Handle other exceptions as needed
            return make_response(jsonify({'errors': ['An error occurred']}), 500)
        
api.add_resource(Restaurants, '/restaurants')
api.add_resource(RestaurantsById, '/restaurants/<int:id>', endpoint='restaurants_by_id')
api.add_resource(Pizzas, '/pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
