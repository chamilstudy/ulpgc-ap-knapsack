from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:

    def __init__(self, index, taken, value, room):
        self.index  =   index
        self.taken  =   taken
        self.value  =   value
        self.room   =   room

    def estimate(self, items):
        est = 0

        for i in items:
            est += i.value

        for i in items:
            if i.index not in self.taken:
                print(i)
                est -= i.value

            if i.index == len(self.taken):
                break

        return est