from unittest.mock import Mock

import pytest

from praktikum.burger import Burger

def test_set_buns_sets_bun():
    burger = Burger()
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun == bun

def test_add_ingredient_adds_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients

def test_remove_ingredient_removes_ingredient():
    burger = Burger()
    ingredient = Mock()
    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)

    assert ingredient not in burger.ingredients

@pytest.mark.parametrize(
    'index, new_index, expected_order',
    [
        (0, 1, [1, 0, 2]),
        (2, 0, [2, 0, 1]),
        (1, 2, [0, 2, 1]),
    ]
)
def test_move_ingredient_moves_ingredient(index, new_index, expected_order):
    burger = Burger()
    ingredients = [Mock(), Mock(), Mock()]

    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    burger.move_ingredient(index, new_index)

    expected = [ingredients[i] for i in expected_order]
    assert burger.ingredients == expected

def test_get_price_returns_correct_price():
    burger = Burger()
    bun = Mock()
    ingredient = Mock()
    bun.get_price.return_value = 100
    ingredient.get_price.return_value = 50
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    result = burger.get_price()

    assert result == 250

def test_get_receipt_returns_correct_receipt():
    burger = Burger()
    bun = Mock()
    ingredient = Mock()

    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    ingredient.get_type.return_value = 'SAUCE'
    ingredient.get_name.return_value = 'hot sauce'
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    result = burger.get_receipt()

    assert result == '(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 250'