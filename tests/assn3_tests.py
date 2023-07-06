from assertions import *

orange_name = 'orange'
spaghetti_name = 'spaghetti'
apple_pie_name = 'apple pie'

resource_dishes = "dishes"
resource_meals = "meals"

# response will keep the id's of the dishes
orange_id = None
spaghetti_id = None
apple_pie_id = None

def test_post_dishes_three_dishes_orange_spaghetti_applepie():
    global orange_id
    global spaghetti_id
    global apple_pie_id

    orange_request_data = {"name": orange_name}
    response_orange = connectionController.http_post(resource_dishes, orange_request_data)

    assert_valid_added_resource(response_orange)

    spaghetti_request_data = {"name": spaghetti_name}
    response_spaghetti = connectionController.http_post(resource_dishes, spaghetti_request_data)

    assert_valid_added_resource(response_spaghetti)

    apple_pie_request_data = {"name": apple_pie_name}

    response_apple_pie = connectionController.http_post(resource_dishes, apple_pie_request_data)

    assert_valid_added_resource(response_apple_pie)

    orange_id = response_orange.json()
    spaghetti_id = response_spaghetti.json()
    apple_pie_id = response_apple_pie.json()

    # checks if all the ids are unique
    assert orange_id != spaghetti_id \
           and orange_id != apple_pie_id \
           and spaghetti_id != apple_pie_id


def test_get_dishes_by_id_orange():
    global orange_id

    response = connectionController.http_get(f"dishes/{orange_id}")
    assert_status_code(response, status_code = 200)
    orange_dish_info = response.json()
    sodium_of_dish = orange_dish_info["sodium"]
    assert 0.9 <= sodium_of_dish <= 1.1

def test_get_dishes_all():
    response = connectionController.http_get(resource_dishes)
    assert_status_code(response, status_code = 200)
    json_object_of_all_dishes = response.json()
    assert len(json_object_of_all_dishes) == 2

def test_post_dishes_with_name_unrecognized_to_ninja():
    response = connectionController.http_post(resource_dishes,{'name': "blah"})
    assert response.status_code == 400 or response.status_code == 404 or response.status_code == 422
    assert response.json() == -3

def test_post_dishes_already_exists_orange():
    response = connectionController.http_post(resource_dishes,{'name': orange_name})
    assert response.status_code == 400 or response.status_code == 404 or response.status_code == 422
    assert response.json() == -2

def test_post_meals_by_name_delicious():
    global orange_id
    global spaghetti_id
    global apple_pie_id

    json_object_of_new_meal = {'name': "delicious", 'appetizer': orange_id,
                  'main': spaghetti_id, 'dessert': apple_pie_id}
    response = connectionController.http_post("meals", json_object_of_new_meal)
    assert_valid_added_resource(response)


def test_get_all_meals():
    response = connectionController.http_get(resource_meals)
    assert_status_code(response,status_code = 200)
    json_object_of_all_meals = response.json()

    assert len(json_object_of_all_meals) == 1

    for meal_id, meal_object in json_object_of_all_meals.items():
        meal_calories = meal_object["cal"]
        assert 400 <= meal_calories <= 500


def test_post_meals_already_exists():
    global orange_id
    global spaghetti_id
    global apple_pie_id

    json_object_of_new_meal = {'name': "delicious", 'appetizer': orange_id,
                               'main': spaghetti_id, 'dessert': apple_pie_id}
    response = connectionController.http_post("meals", json_object_of_new_meal)
    assert response.status_code == 400 or response.status_code == 422
    assert response.json() == -2
