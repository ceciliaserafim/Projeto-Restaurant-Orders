from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish_pizza = Dish("pizza", 40.00)

    assert dish_pizza == Dish("pizza", 40.00)
    assert dish_pizza != Dish("pizzahjgx", 20.99)

    assert dish_pizza.name == "pizza"

    assert hash(dish_pizza) == hash(Dish("pizza", 40.00))
    assert hash(dish_pizza) != hash(Dish("sopa", 30.00))

    assert repr(dish_pizza) == "Dish('pizza', R$40.00)"

    ingred_farinha = Ingredient("farinha")
    dish_pizza.add_ingredient_dependency(ingred_farinha, 8)
    assert dish_pizza.recipe == {ingred_farinha: 8}

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
            ):
        Dish("pizzahjgx", -20.99)

    assert dish_pizza.get_restrictions() == {Restriction.GLUTEN}
    assert dish_pizza.get_ingredients() == {ingred_farinha}
