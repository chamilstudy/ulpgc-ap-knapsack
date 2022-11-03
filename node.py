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

        for i in range(0, self.index):
            if items[i].index not in self.taken:
                est -= items[i].value
                
        return est

#for i in items:
#            est += i.value
#
#        if len(self.taken) > 0:
#            for i in range(0, self.taken[len(self.taken) - 1]):
#                if i not in self.taken:
#                    est -= items[i].value
#        else:
#            for i in range(0, self.index):
#                est -= items[i].value