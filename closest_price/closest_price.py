def the_price_is_right(price_list, target_price):
    if not price_list:
        return [], target_price

    current_choices = []
    price_left = target_price

    for index, item_price in enumerate(price_list):
        if item_price > target_price:
            continue
        else:
            choices, rest_price = the_price_is_right(
                price_list[index+1::], target_price-item_price)
            choices.append(item_price)
            if rest_price < price_left:
                current_choices = choices
                price_left = rest_price
    return current_choices, price_left
