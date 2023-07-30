from mylib.logistics import distance_between_two_points, cities_list, CITIES


def test_distance_between_two_points():
    """
    This function tests the distance_between_two_points function
    """
    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 2450.9503446683375


def test_cities_list():
    """
    This function tests the print_cities function
    """
    assert "New York" in cities_list()