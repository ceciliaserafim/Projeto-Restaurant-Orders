import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as openfile:
            data = csv.DictReader(openfile)
            list_dishes = {}

            for row in data:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_quantity = int(row["recipe_amount"])
                ingredient = Ingredient(ingredient_name)
                dish = list_dishes.get(dish_name)

                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    list_dishes[dish_name] = dish
                    self.dishes.add(dish)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def _validate_csv(self, source_path: str):
        self.is_csv(source_path)

        if not isinstance(source_path, str):
            raise TypeError("Não é uma instancia")
        if not source_path.endswith(".csv"):
            raise TypeError("Não é um arquivo CSV")
