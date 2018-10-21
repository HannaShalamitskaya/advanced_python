from collections import namedtuple
from contextlib import suppress
from functools import reduce
from itertools import chain
from itertools import starmap
from itertools import takewhile
import os

MAX_WEIGHT = 400
DATA_PATH = "data"


def read_items(data_file="items.csv"):
    # read information about items from the file
    with open(os.path.join(DATA_PATH, data_file)) as rf:
        BackPackItem = namedtuple("Item", rf.readline())
        items = []
        for line in rf.readlines():
            data = line[:-1].split(',')
            with suppress(ValueError):
                data = list(chain(data[:1], map(int, data[1:])))
                items.append(BackPackItem(*data))
    return items


def calculate_items_efficiency(items):
    # calculate efficiency for every items
    GreedyItem = namedtuple("GreedyItem", "item efficiency")
    greedy_items = starmap(GreedyItem,
                           [(i, i.value / i.weight) for i in items])
    greedy_items = sorted(greedy_items, key=lambda i: i.efficiency,
                          reverse=True)
    return greedy_items


def pack_items(greedy_items):
    total_weight = 0
    packed_items = []

    for each in greedy_items:
        if total_weight + each.item.weight <= MAX_WEIGHT:
            total_weight += each.item.weight
            packed_items.append(each.item)

    total_value = reduce(lambda a, b: a + b, [i.value for i in packed_items])
    print("Calculated valuable:", total_value, "weight:", total_weight)

    return {"total_weight": total_weight,
            "total_value": total_value,
            "packed_items": packed_items}


def check_most_valuable_items(items, solution):
    # try to cover an exceptional case
    # when value of one item is more then calculated valuable
    # for example add to the items.csv:
    # magic box,390,2000
    exceptional = list(takewhile(
        lambda i: i.value > solution["total_value"] and i.weight < MAX_WEIGHT,
        sorted(items, key=lambda i: i.value, reverse=True)))

    if exceptional:
        solution["total_value"] = exceptional[0].value
        solution["total_weight"] = exceptional[0].weight
        solution["packed_items"] = exceptional[:1]

    return solution


def print_results(solution):
    print("Got items:")
    for each in solution["packed_items"]:
        print(each.name, each.weight, each.value)
    print("Result:")
    print("valuable:", solution["total_value"],
          "weight:", solution["total_weight"])


def greedy_solution():
    items = read_items()
    solution = pack_items(calculate_items_efficiency(items))
    solution = check_most_valuable_items(items, solution)
    print_results(solution)


if __name__ == "__main__":
    greedy_solution()
