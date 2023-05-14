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
    print('|U| = ' + str(len(universe)))
    print('|C| = ' + str(len(collection)))
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

c_2 = [[4, 7, 10, 13, 16, 17, 18, 19, 20, 27],
       [0, 1, 38, 11, 18, 24, 25, 31],
       [36, 6, 40, 19, 24, 29],
       [33, 34, 38, 39, 8, 11, 14, 15, 22],
       [37, 38, 39, 15, 19, 26, 30],
       [0, 3, 6, 42, 12, 16, 24],
       [33, 39, 14, 24, 30],
       [1, 2, 4, 5, 13, 16, 20, 25],
       [14],
       [1, 34, 7, 14, 16, 17, 22, 23],
       [33, 11],
       [0, 2, 35, 36, 37, 40, 8, 43, 13],
       [9, 4, 33, 23],
       [1, 3, 4, 7, 9, 13, 16, 28],
       [37, 7, 8, 41, 43, 18, 21, 27, 28],
       [1, 39, 8, 42, 10, 15, 19, 22, 28],
       [0, 1, 3, 4, 40, 41, 10, 11, 8, 13, 15],
       [32, 9, 23],
       [33, 2, 3, 35, 9, 13, 16, 17],
       [1, 3, 5, 38],
       [27],
       [33, 39, 9, 15, 27],
       [34, 7, 9, 10, 11, 42, 15, 24],
       [1, 38, 7, 39, 17]]

solution_1_brute_force = [3, 8, 11, 13, 14, 16, 19, 20, 21, 23]
solution_1_greedy = [3, 20, 13, 23, 0, 5, 2, 4, 8, 11, 12]

solution_2_brute_force = [1, 2, 4, 5, 7, 9, 14, 17, 18, 22]
solution_2_greedy = [16, 0, 3, 11, 5, 17, 1, 4, 14, 2, 7]

instances = [(u_1, c_1, solution_1_brute_force), (u_1, c_2, solution_2_brute_force)]
