'''Module with useful functions for the 
Set Cover problem.'''

import random


def create_collection(universe: list) -> list:
    '''Returns a collection of subsets of the `universe`.'''
    subsets = []
    for i in range(24):
        subset = set()
        subset_size = random.randint(1, 11)
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


def verification_algorithm(universe: list, collection: list, certificate: list) -> bool:
    '''Returns true if the given `certificate` is a solution for
    the given instance of the set cover problem. A certificate is 
    a list with indices of the subsets of the collection.'''
    assert len(collection) >= len(certificate)
    for i in certificate:
        assert i < len(collection)
    u_set = set(universe)
    proposal_cover = set()
    for i in certificate:
        for element in collection[i]:
            proposal_cover.add(element)
    return proposal_cover == u_set

'''
u = list(range(44))
c = create_collection(u)
print_instance(u, c)
print(has_cover(u, c))
'''

u_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
       23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
c_1 = [[3, 36, 37, 39, 8, 10, 13, 18, 26, 27],
       [0, 27, 5],
       [9, 43, 14, 17, 19, 23],
       [35, 3, 38, 10, 42, 15, 16, 20, 21, 24, 29],
       [38, 1, 28, 30],
       [3, 36, 37, 9, 10, 43, 12, 13, 11, 17],
       [32, 16],
       [35, 37, 5, 41, 13],
       [33, 7],
       [6, 7, 8, 9, 10, 23, 24, 31],
       [38, 6, 42, 43, 24, 25],
       [34, 41, 10, 11, 25, 26],
       [4, 5, 6, 36, 18, 27],
       [0, 5, 39, 40, 41, 7, 13, 28],
       [36, 37, 7, 40, 42, 12, 13, 16, 18, 21, 23],
       [41, 21, 6],
       [8, 27, 5, 22],
       [5],
       [26, 3, 30],
       [3, 4, 39, 9, 10, 22],
       [35, 36, 6, 9, 17, 18, 22, 27, 30, 31],
       [0, 1, 5],
       [0, 40, 43, 14, 20, 23],
       [32, 0, 2, 36, 38, 43, 14, 19, 20, 25]]

solution_1_brute_force = [3, 8, 11, 13, 14, 16, 19, 20, 21, 23]
solution_1_greedy = [3, 20, 13, 23, 0, 5, 2, 4, 8, 11, 12]

print(verification_algorithm(u_1, c_1, solution_1_brute_force))
print(verification_algorithm(u_1, c_1, solution_1_greedy))

