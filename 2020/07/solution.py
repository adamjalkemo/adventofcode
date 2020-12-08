from pathlib import Path

with Path("input.txt").open() as f:
    bag_descriptions = f.read().splitlines()


print("Part 1:")
split_bags = [
    bag_description.split(" contain ") for bag_description in bag_descriptions
]
contained_bags_by_bag = {k.replace(" bags", ""): v for k, v in split_bags}

outer_bags = {"shiny gold"}
while True:
    prev_outer_bags = set(outer_bags)
    for k, v in contained_bags_by_bag.items():
        for bag in outer_bags:
            if bag in v:
                outer_bags.add(k)
                break
    if prev_outer_bags == outer_bags:
        break
outer_bags.remove("shiny gold")
print(
    f"Solution: there are {len(outer_bags)} bags that eventually contain a shiny gold bag"
)
assert len(outer_bags) == 213


print("Part 2:")
print(f"Solution: ")

def get_number_of_contained_bags(bag):
    number_of_bags = 0

    bags_in_bag = contained_bags_by_bag[bag]
    if "no other bags" in bags_in_bag:
        return number_of_bags

    for qty_and_bag in bags_in_bag.split(","):
        qty_and_bag = qty_and_bag.replace("bags", "").replace("bag", "").strip(". ")
        qty_str, bag1, bag2 = qty_and_bag.split(" ")
        qty = int(qty_str)
        bag = " ".join((bag1, bag2))
        bags_in_bag = get_number_of_contained_bags(bag)
        number_of_bags += qty * (1 + bags_in_bag)
    return number_of_bags

print(get_number_of_contained_bags("shiny gold"))
assert get_number_of_contained_bags("shiny gold") == 38426