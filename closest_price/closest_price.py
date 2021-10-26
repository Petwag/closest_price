def the_price_is_right(price_list, target_price):
    if not price_list:
        return [], target_price

    current_choices = []
    price_left = target_price

    for index, item_price in enumerate(price_list):
        if item_price > target_price:
            continue
        else:
            choices, rest_price = the_price_is_right(price_list[index+1::], target_price-item_price)
            choices.append(item_price)
            if rest_price < price_left:
                current_choices = choices
                price_left = rest_price
    return current_choices, price_left

def main():
    target_price = 28

    list_price = [
        11.95,
        25,
        19.95,
        4.95,
        4.95,
        4.95,
        4.95,
        5.25,
        5.50,
        12.95,
        12.95
    ]

    print(the_price_is_right(list_price, target_price))

if __name__ == "__main__":
    main()
