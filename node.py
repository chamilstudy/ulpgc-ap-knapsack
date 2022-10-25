from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    index = taken = value = room = 0

    def __init__(self, index, taken, value, room):
        self.index  =   index
        self.taken  =   taken
        self.value  =   value
        self.room   =   room

    def estimate(self, items):
        est = 0
        for item in items:
                est = est + self.value
        return est

#3 10
#45 5  83
#35 3  83
#48 8  35