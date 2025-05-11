import Lab2

def test_find_min_max():
    return Lab2.find_min_max([5, 1, 9, 3]) == [1, 9]

def test_calc_average():
    return Lab2.calc_average([10, 20, 30]) == 20

def test_calc_median_temperature():
    return Lab2.calc_median_temperature([30.5, 25.5, 29.0]) == 29.0
