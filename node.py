from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    index = taken = value = room = 0

    def __init__(self, index, taken, value, room):
        pass

    def estimate(self, items):
        return 0