from collections import Counter

sample = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

with open("input.txt") as f:
    input_data = f.read().splitlines()


def intersections(data):
    all_ingredients = set()
    allergens_by_possible_ingredients = {}
    ingredient_count = Counter()
    for line in data:
        ingredients, allergens = line.split("(contains ")
        allergens = allergens.strip(")").split(", ")
        ingredients = ingredients.strip().split(" ")
        all_ingredients.update(ingredients)
        ingredient_count.update(ingredients)

        for allergen in allergens:
            if allergen not in allergens_by_possible_ingredients:
                allergens_by_possible_ingredients[allergen] = set(ingredients)
            else:
                allergens_by_possible_ingredients[
                    allergen
                ] = allergens_by_possible_ingredients[allergen].intersection(
                    ingredients
                )

    possible_allergen_ingredients_flat = {
        ingredient
        for ingredients in allergens_by_possible_ingredients.values()
        for ingredient in ingredients
    }
    ingredients_not_allergens = all_ingredients - possible_allergen_ingredients_flat

    count = sum(
        ingredient_count[ingredient] for ingredient in ingredients_not_allergens
    )

    allergent_by_ingredient = solve_greedy(allergens_by_possible_ingredients)

    sorted_allergent_by_ingredient = {
        k: v
        for k, v in sorted(allergent_by_ingredient.items(), key=lambda item: item[1])
    }

    dangerous_str = ",".join(sorted_allergent_by_ingredient.keys())

    return [count, dangerous_str]


def solve_greedy(allergens_by_possible_ingredients):
    allergens_by_possible_ingredients = sort_by_number_of_ingredients(
        allergens_by_possible_ingredients
    )
    allergent_by_ingredient = {}
    allergens = list(allergens_by_possible_ingredients)
    while allergens:
        allergen = allergens.pop(0)
        for ingredient in allergens_by_possible_ingredients[allergen]:
            if ingredient not in allergent_by_ingredient:
                allergent_by_ingredient[ingredient] = allergen
                del allergens_by_possible_ingredients[allergen]
                allergens_by_possible_ingredients = remove_ingredient(
                    allergens_by_possible_ingredients, ingredient
                )
                allergens_by_possible_ingredients = sort_by_number_of_ingredients(
                    allergens_by_possible_ingredients
                )
                allergens = list(allergens_by_possible_ingredients)
                break
        else:
            raise NotImplementedError
    return allergent_by_ingredient


def sort_by_number_of_ingredients(allergens_by_possible_ingredients):
    return {
        k: v
        for k, v in sorted(
            allergens_by_possible_ingredients.items(), key=lambda item: len(item[1])
        )
    }


def remove_ingredient(allergens_by_possible_ingredients, ingredient_to_remove):
    return {
        allergen: {
            ingredient
            for ingredient in ingredients
            if ingredient != ingredient_to_remove
        }
        for allergen, ingredients in allergens_by_possible_ingredients.items()
    }


def part1_test():
    assert intersections(sample)[0] == 5


def part1():
    assert intersections(input_data)[0] == 2614


def part2_test():
    assert intersections(sample)[1] == "mxmxvkd,sqjhc,fvjkl"


def part2():
    assert intersections(input_data)[1] == "qhvz,kbcpn,fzsl,mjzrj,bmj,mksmf,gptv,kgkrhg"


part1_test()
part1()
part2_test()
part2()
