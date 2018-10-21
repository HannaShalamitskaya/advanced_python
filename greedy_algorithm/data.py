from collections import namedtuple
from contextlib import suppress
from itertools import chain
from itertools import starmap


def read_data_from_file(file_name):
    # read information about items from the file
    with open(file_name) as rf:
        BackPackItem = namedtuple("Item", rf.readline())
        items = []
        for line in rf.readlines():
            data = line[:-1].split(',')
            with suppress(ValueError):
                data = list(chain(data[:1], map(int, data[1:])))
                items.append(BackPackItem(*data))
    return items


def calculate_efficiency(items):
    # calculate efficiency for every items
    GreedyItem = namedtuple("GreedyItem", "name weight value efficiency")
    greedy_items = list(starmap(GreedyItem,
                                [(*i, i.value / i.weight) for i in items]))
    greedy_items = sorted(greedy_items, key=lambda i: i.efficiency,
                          reverse=True)
    return greedy_items


def get_items(file_name):
    items = calculate_efficiency(read_data_from_file(file_name))
    return items
