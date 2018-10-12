from collections import namedtuple
from contextlib import suppress
from functools import reduce
from itertools import chain
from itertools import starmap
from itertools import takewhile

MAX_WEIGHT = 400


# read information about items from the file
with open("items.csv") as rf:
    BackPackItem = namedtuple("Item", rf.readline())
    items = []
    for line in rf.readlines():
        data = line[:-1].split(',')
        with suppress(ValueError):
            data = list(chain(data[:1], map(int, data[1:])))
            items.append(BackPackItem(*data))

# calculate efficiency for every items
GreedyItem = namedtuple("GreedyItem", "item efficiency")
greedy_items = starmap(GreedyItem, [(i, i.value / i.weight) for i in items])
greedy_items = sorted(greedy_items, key=lambda i: i.efficiency, reverse=True)

# pack the most significant items using greedy algorithm
weight_greedy = 0
value_greedy = 0
packed_items = []
for each in greedy_items:
    if weight_greedy + each.item.weight <= MAX_WEIGHT:
        weight_greedy += each.item.weight
        packed_items.append(each.item)

value_greedy = reduce(lambda a, b: a + b, [i.value for i in packed_items])
print("Calculated valuable:", value_greedy, "weight:", weight_greedy)

# try to cover an exceptional case
# when value of one item is more then calculated valuable
# for example add to the items.csv:
# magic box,390,2000
exceptional = list(takewhile(
    lambda i: i.value > value_greedy and i.weight < MAX_WEIGHT,
    sorted(items, key=lambda i: i.value, reverse=True)))

if exceptional:
    value_greedy = exceptional[0].value
    weight_greedy = exceptional[0].weight
    packed_items = exceptional[:1]

print("Got items:")
for each in packed_items:
    print(each.name, each.weight, each.value)
print("Result:")
print("valuable:", value_greedy, "weight:", weight_greedy)
