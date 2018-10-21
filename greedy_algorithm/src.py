from functools import reduce
from greedy_algorithm.data import get_items
from itertools import takewhile
import os


MAX_WEIGHT = 400
DATA_PATH = "data"


def pack(greedy_items):
    # pack the most significant items using greedy algorithm
    weight = 0
    got_items = []

    for item in greedy_items:
        if weight + item.weight <= MAX_WEIGHT:
            weight += item.weight
            got_items.append(item)

    return got_items


def greedy_exceptional_case(items, got_items):
    """
    try to cover an exceptional case
    when value of one item is more then calculated valuable
    for example add to the items.csv:
    magic box,390,2000
    """
    value = reduce(lambda a, b: a + b, [i.value for i in got_items])
    exceptional = list(takewhile(
        lambda i: i.value > value and i.weight < MAX_WEIGHT,
        sorted(items, key=lambda i: i.value, reverse=True)))

    if exceptional:
        got_items = exceptional[:1]

    return got_items


def pack_greedy(file_name="items.csv"):
    items = get_items(os.path.join(DATA_PATH, file_name))
    got_items = pack(items)
    got_items = greedy_exceptional_case(items, got_items)

    return got_items


if __name__ == "__main__":
    import doctest
    doctest.testfile("test_pack_greedy.txt")

    packed_items = pack_greedy()
    print("Got items:")
    for each in packed_items:
        print(each.name, each.weight, each.value)

    total_value = reduce(lambda a, b: a + b, [i.value for i in packed_items])
    total_weight = reduce(lambda a, b: a + b, [i.weight for i in packed_items])
    print("valuable:", total_value, "weight:", total_weight)
