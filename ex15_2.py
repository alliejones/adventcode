# test code

# def generate_all_proportions():
#     for a in xrange(101):
#         yield (a, 100 - a)

# ingredients = [
#     (-1, -2, 6, 3, 8),
#     (2, 3, -2, -1, 3)
# ]

def generate_all_proportions():
    for a in xrange(101):
        for b in xrange(100 - a):
            for c in xrange(100 - a - b):
                yield (a, b, c, 100 - a - b - c)

ingredients = [
    (3, 0, 0, -3, 2),
    (-3, 3, 0, 0, 9),
    (-1, 0, 4, 0, 1),
    (0, 0, -2, 2, 8)
]

def calc_cookie_score(proportions):
    property_count = len(ingredients[0]) - 1 # skip last item (calories)
    total = 1
    for property_index in range(property_count):
        val = sum([ing[property_index]*proportions[ing_index] for ing_index, ing in enumerate(ingredients)])
        if val > 0:
            total *= val
        else:
            total *= 0
    calories = sum([ing[property_count]*proportions[ing_index] for ing_index, ing in enumerate(ingredients)])
    if calories == 500:
        return total
    else:
        return 0 # if it isn't 500 calories assume a score of zero

print max([calc_cookie_score(p) for p in generate_all_proportions()])
