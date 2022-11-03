from collections import namedtuple

from node import *
from solve import *

#first_line = input().split()
#item_count = int(first_line[0])
#capacity = int(first_line[1])
    
#items = []
#for i in range(1, item_count+1):
#    line = input()
#    parts = line.split()
#    items.append(Item(i-1, int(parts[0]), int(parts[1])))

def test():
    capacity = 10
    items = [Item(1, 45, 5),
            Item(2, 48, 8),
            Item(3, 35, 3)]
    print(Node(1,[],0, capacity).estimate(items))
    print(Node(2,[1],items[1].value, capacity - items[1].weight).estimate(items))
    print(Node(3,[2],items[1].value,capacity - items[1].weight).estimate(items))

def test2():
    capacity = 10
    items = [Item(1, 45, 5),
            Item(2, 48, 8),
            Item(3, 35, 3)]
            
    value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)
    print(visiting_order)
    print(value)
    print(taken)

    capacity = 10
    items = [Item(1, 45, 5),
            Item(2, 48, 8),
            Item(3, 35, 3),
            Item(4, 55, 3),
            Item(5, 15, 7)]

    value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)
    print()
    print(visiting_order)
    print(value)
    print(taken)

test2()

0, 1, 2, 2, 3, 3, 1, 2, 3, 3, 2

0, 1, 2, 2, 3, 4, 4, 3, 4, 4, 5, 5, 1, 2, 3, 3, 4, 4, 5, 5, 2, 3, 3, 4, 4, 5, 5
0, 1, 2, 2, 3, 4, 4, 5, 5, 3, 4, 5, 5, 4, 5, 5, 1, 2, 3, 3, 4, 4, 5, 5, 2, 3, 4, 5, 5, 4, 5, 5, 3, 4, 4, 5, 5