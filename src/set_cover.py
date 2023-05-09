'''Module with useful functions for the 
Set Cover problem.'''

import random


def create_collection(universe: list) -> list:
    '''Returns a collection of subsets of the `universe`.'''
    subsets = []
    for i in range(15):
        subset = set()
        subset_size = random.randint(1, 15)
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
