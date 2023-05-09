'''Module with useful functions for the 
Set Cover problem.'''

import random


def create_collection(universe: list) -> list:
    '''Returns a collection of subsets of the `universe`.'''
    subsets = []
    for i in range(15):
        subset = set()
        subset_size = random.randint(1, 12)
        while len(subset) < subset_size:
            subset.add(random.choice(universe))
        subsets.append(list(subset))
    return subsets


def has_cover(universe: list, collection: list) -> bool:
    '''Returns true if exists a cover in `collection` for 
    the `universe`.'''
    aux_set = set()
    for subset in collection:
        for element in subset:
            aux_set.add(element)
    return aux_set == set(universe)


def correct_instance(universe: list, collection: list) -> bool:
    '''Returns true it the given instance of the SC problem
    is correct.'''
    if len(universe) != len(set(universe)):
        return False
    for subset in collection:
        if len(subset) != len(set(subset)):
            return False
    return has_cover(universe, collection)


def print_instance(universe: list, collection: list) -> None:
    '''Prints in console the given instance of 
    the set cover problem.'''
    print('U = ', end='')
    print(universe)
    print('C = \n[' + str(collection[0]) + ',')
    for i in range(1, len(collection)):
        print(str(collection[i]), end='')
        if i == len(collection) - 1:
            print(']')
        else:
            print(',')


u = list(range(30))
c = create_collection(u)
print_instance(u, c)
print(has_cover(u, c))

u_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
       16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
c_1 = [[9, 17, 19, 21, 23, 27],
       [7, 12, 15, 18, 21, 22, 25, 27, 29],
       [1, 8, 11, 13, 15, 17, 20, 23, 26, 27],
       [7, 9, 16, 23, 27],
       [16],
       [2, 5, 7, 9, 11, 20, 21, 22, 24, 28],
       [3, 5, 6, 7, 8, 9, 11, 15, 26, 28],
       [1, 8, 9, 11, 23],
       [1],
       [5, 7, 8, 11, 18, 19, 27, 28],
       [2, 7, 13, 14, 18],
       [4, 6, 9, 10, 11, 13, 15, 18, 20, 22, 25, 28],
       [4, 6, 8, 10, 19, 20, 22, 24, 25, 28, 29],
       [0, 14, 19, 22, 23, 24],
       [2, 8, 12, 14, 15, 21, 25, 29]]
