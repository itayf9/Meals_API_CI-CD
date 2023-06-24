import connectionController
from assertions import *

orange_name = 'orange'
spaghetti_name = 'spaghetti'
apple_pie_name = 'apple pie'

resource_dishes = "dishes"
resource_meals = "meals"

def test_post_dishes_three_dishes_orange_spaghetti_applepie():
    orange_request_data = {"name": orange_name}
    response_orange = connectionController.http_post(resource_dishes, orange_request_data)

    assert_valid_added_resource(response_orange)

    spaghetti_request_data = {"name": spaghetti_name}
    response_spaghetti = connectionController.http_post(resource_dishes, spaghetti_request_data)

    assert_valid_added_resource(response_spaghetti)

    apple_pie_request_data = {"name": apple_pie_name}
    response_apple_pie = connectionController.http_post(resource_dishes, apple_pie_request_data)

    assert_valid_added_resource(response_apple_pie)

    # checks if all the ids are unique
    assert response_orange != response_spaghetti \
           and response_orange != response_apple_pie \
           and response_spaghetti != response_apple_pie


def test_get_dishes_by_id_orange():
    pass


def test_get_dishes_all():
    pass


def test_post_dishes_with_name_unrecognized_to_ninja():
    pass


def test_post_dishes_already_exists_orange():
    pass


def test_post_meals_by_name_delicious():
    pass


def test_get_all_meals():
    pass


def test_post_meals_already_exists():
    pass