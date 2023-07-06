import connectionController as cc

dishes_resource = "dishes"


def handle_query_txt(input_file_path: str):
    query_file = open(input_file_path)
    lines = query_file.read().splitlines()

    text_of_results_messages = ""

    for dish_name in lines:
        response_from_post_dish = cc.http_post(dishes_resource, {"name": dish_name})
        if response_from_post_dish.status_code != 201:
            text_of_results_messages += f"{response_from_post_dish.status_code},{response_from_post_dish.json()}\n"
            continue

        id_of_created_dish = response_from_post_dish.json()
        response_from_get_dish_by_id = cc.http_get(f"dishes/{id_of_created_dish}")
        if response_from_get_dish_by_id.status_code != 200:
            text_of_results_messages += f"{response_from_get_dish_by_id.status_code},{response_from_get_dish_by_id.json()}\n"
            continue

        created_dish = response_from_get_dish_by_id.json()
        cal = created_dish["cal"]
        sodium = created_dish["sodium"]
        sugar = created_dish["sugar"]

        result_message_of_created_dish = f"{dish_name} contains {format(cal, '.6f')} calories, {format(sodium, '.6f')} mgs of sodium, and {format(sugar, '.6f')} grams of sugar\n"
        text_of_results_messages += result_message_of_created_dish

    print(text_of_results_messages)
