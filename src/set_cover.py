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


def has_solution(universe: list, collection: list) -> bool:
    '''Returns true if exists a cover in `collection` for 
    the `universe`'''
    aux_set = set()
    for subset in collection:
        for element in subset:
            aux_set.add(element)
    return aux_set == set(universe)


u = list(range(30))
c = create_collection(u)
print(c)
print(has_solution(u, c))
