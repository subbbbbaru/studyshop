import pytest
from studyshop.pricing import total_cost


def test_without_discount():
    assert total_cost(100, 3) == 300


def test_with_discount():
    assert total_cost(200, 2, 25) == 300


def test_full_discount():
    assert total_cost(100, 1, 100) == 0


@pytest.mark.parametrize("args", [(-1, 2, 0), (100, 0, 0), (100, 1, 101)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        total_cost(*args)
