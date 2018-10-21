from itertools import takewhile
from itertools import accumulate
from functools import reduce
import os

from greedy_algorithm.data import get_items


MAX_WEIGHT = 400
DATA_PATH = "data"


def pack_greedy(file_name="items.csv"):
    items = get_items(os.path.join(DATA_PATH, file_name))
    solution = items[: len(
        list(takewhile(lambda x: x < MAX_WEIGHT,
                       accumulate([0] + items, lambda x, y: x+y[1])))) - 1]

    return solution


if __name__ == "__main__":
    packed_items = pack_greedy()
    print("Got items:")
    for each in packed_items:
        print(each.name, each.weight, each.value)

    total_value = reduce(lambda a, b: a + b, [i.value for i in packed_items])
    total_weight = reduce(lambda a, b: a + b, [i.weight for i in packed_items])
    print("valuable:", total_value, "weight:", total_weight)
