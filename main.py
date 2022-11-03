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


capacity = 10
items = [Item(0, 45, 5),
        Item(1, 48, 8),
        Item(2, 35, 3)]
        
value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)
print(visiting_order)
print(value)
print(taken)

capacity = 10
items = [Item(0, 45, 5),
        Item(1, 48, 8),
        Item(2, 35, 3),
        Item(3, 55, 3),
        Item(4, 15, 7)]

value, taken, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)
print()
print(visiting_order)
print(value)
print(taken)

0, 1, 2, 2, 3, 3, 1, 2, 3, 3, 2
0, 1, 2, 2, 3, 3, 1, 2, 3, 3, 2, 3, 3
0, 1, 2, 2, 3, 4, 4, 5, 5, 3, 4, 5, 5, 4, 1, 2, 3, 3, 4, 4, 2, 3, 4, 5, 5, 4, 3
0, 1, 2, 2, 3, 4, 4, 5, 5, 3, 4, 5, 5, 4, 5, 5, 1, 2, 3, 3, 4, 4, 5, 5, 2, 3, 4, 5, 5, 4, 5, 5, 3, 4, 4, 5, 5