from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    wheat_flour = Ingredient("farinha")
    tomato = Ingredient("tomate")
    expected_ing = Ingredient("tomate")

    assert tomato == expected_ing
    assert tomato.name == "tomate"
    assert str(tomato) == "Ingredient('tomate')"
    assert hash(tomato) == hash(expected_ing)
    assert hash(tomato) != hash(Ingredient("presunto"))
    assert wheat_flour.restrictions == {Restriction.GLUTEN}
