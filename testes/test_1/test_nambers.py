import pytest
from nambers import list_of_numbers


@pytest.mark.parametrize("n, expected", [
    (1, [1]),
    (5, [1, 2, 3, 4, 5]),
    (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_list_of_numbers(n, expected):
    assert list_of_numbers(n) == expected