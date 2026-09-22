from greatest_smallest import two_extremes


def test_example():
    xs = [3, -7, 10, 8, 5, -4, 10, -2, 3, -9, 10]
    assert two_extremes(xs) == (10, 10, -9, -7)
