from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    index = taken = value = room = 0

    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room

    def estimate(self, items):
        est = 0

        for i in items:
            est = i.value + est
            
        return est - self.value