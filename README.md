## Pizza API Challenge
A simple Flask-based RESTful API for managing restaurants, pizzas, and their associations.

### Setup Instructions
1. Clone the repository
git clone git@github.com:zawzawke/pizza-api-challenge.git
cd pizza-api-challenge

2. Install dependencies using pipenv
pipenv install
pipenv shell

3. Run the application
flask run

#### Database Setup
1. Initializa migrations
flask db init

2. Generate migration script
flask db migrate -m "Initial migration"

3. Apply migration
flask db upgrade

4. Seed the database
python3 -m server.seed

### API Routes Summary
Method	     Endpoint	        Description
GET	         /restaurants	    Get a list of all restaurants
GET	        /restaurants/<id>	Get a single restaurant with pizzas
DELETE	   /restaurants/<id>	Delete a restaurant
GET	      /pizzas	            Get a list of all pizzas
POST	 /restaurant_pizzas	    Create a restaurant-pizza relationship

### Example Requests & Responses
1. GET /restaurants
Response
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  },
  ...
]

2. GET /restaurants/1
Response
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Basil, Mozzarella"
    },
    ...
  ]
}

3. DELETE /restaurants/1
Response: 204 No Content (successfully deleted)

4. GET /pizzas
Response
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Basil, Mozzarella"
  },
  ...
]

5. POST /restaurant_pizzas
Request
{
  "price": 20,
  "pizza_id": 1,
  "restaurant_id": 1
}

Response
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St"
}

#### Validation Rules
- price must be between 1 and 30
- pizza_id and restaurant_id must exist
- name and address are required for Restaurant
- name and ingredients are required for Pizza

#### Testing with Postman
1. Import collection
- Open Postman
- Click Import > Choose challenge-1-pizzas.postman_collection.json

2. Test endpoints
- Run requests using the imported collection
- Confirm expected status codes:
200 OK for GET
201 Created for successful POST
204 No Content for DELETE
400 Bad Request for validation errors

Author - Paul Simiyu