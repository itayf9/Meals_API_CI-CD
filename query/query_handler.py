import requests

import tests.connectionController as tcc

dishes_resource = "dishes"


def handle_query_txt(input_file_path: str):
    query_file = open(input_file_path)
    lines = query_file.readlines()

    text_of_results_messages = ""

    for dish_name in lines:
        response_from_post_dish = tcc.http_post(dishes_resource, dish_name)
        if response_from_post_dish.status_code != 201:
            exit(1)

        id_of_created_dish = response_from_post_dish.json()
        response_from_get_dish_by_id = tcc.http_get(f"dishes/{id_of_created_dish}")
        if response_from_get_dish_by_id != 200:
            exit(1)

        created_dish = response_from_get_dish_by_id.json()
        cal = created_dish["cal"]
        sodium = created_dish["sodium"]
        sugar = created_dish["sugar"]

        result_message_of_created_dish = f"{dish_name} contains {cal} calories, {sodium} mgs of sodium, and {sugar} grams of sugar\n"
        text_of_results_messages += result_message_of_created_dish

    print(text_of_results_messages)
