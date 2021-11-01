from closest_price.closest_price import the_price_is_right


def test_closest_price():
    # correct case
    choices, rest = the_price_is_right([10, 20, 31], 30)
    assert sorted(choices) == sorted([10, 20])
    assert rest == 0

    # case where values are higher than the target
    choices, rest = the_price_is_right([100, 200, 31], 30)
    assert sorted(choices) == sorted([])
    assert rest == 30

    # case values are not flaot
    try:
        choices, rest = the_price_is_right(["100"], 30)
    except TypeError as e:
        assert isinstance(e, TypeError)
