import random
lottery_numbers = set(random.sample(list(range(22)), 6))
print(f"lottery_numbers: {lottery_numbers}")

# 1, 3, 5, 7, 11, 20
players = [
    ("OM",{1, 5, 8, 10, 12, 18}),
    ("Nicolle", {3, 12, 2, 9, 7, 5}),
    ("Cris", {7, 11, 18, 6, 9, 3})
]

for name, numbers in players:
    # print(names, numbers)
    intersection = lottery_numbers.intersection(numbers)
    # print(intersection)

    print(f"{name} won {len(intersection)}.")




# Om won 2.
# Nicolle won 3.
# Cris won 3.

