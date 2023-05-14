'''Module with useful functions for the 
Set Cover problem.'''

import random


def create_collection(universe: list) -> list:
    '''Returns a collection of subsets of the `universe`.'''
    subsets = []
    for i in range(23):
        subset = set()
        subset_size = random.randint(1, 20)
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
u = list(range(88))
c = create_collection(u)
print_instance(u, c)
print(has_cover(u, c))
'''

u_1 = list(range(44))

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

u_2 = list(range(88))

c_3 = [[35, 69, 41, 52, 30, 59, 62, 63],
       [0, 2, 4, 11, 16, 23, 27, 36, 37, 43, 45,
           46, 52, 56, 62, 65, 66, 68, 71, 74],
       [16, 30],
       [33, 35, 73, 42, 14, 49, 53, 26, 63],
       [65, 23, 62, 49],
       [37, 6, 75, 43, 14, 80],
       [66, 34, 69, 70, 48, 53],
       [32, 34, 37, 71, 12, 44, 15, 18, 87, 60, 29],
       [1, 10, 13, 22, 25, 27, 28, 30, 46, 50, 57,
        64, 68, 69, 71, 73, 78, 81, 85, 86],
       [0],
       [65, 2, 4, 37, 20, 53, 56, 61],
       [3, 6, 14, 16, 18, 26, 34, 35, 49, 52, 60, 65, 68, 69, 77, 79, 83, 85, 86],
       [66, 4, 37, 8, 41, 42, 75, 9, 77, 55],
       [68, 7, 18, 83, 21, 87, 23, 56, 25, 58, 59, 29],
       [42, 3],
       [64, 67, 68, 37, 36, 8, 40, 10, 43, 76, 42, 59, 48, 22, 55, 27, 63],
       [66, 36, 7, 40, 74, 79, 29, 19, 84, 23, 59, 61, 63],
       [65, 1, 33, 7, 72, 73, 44, 77, 15, 84, 55, 87, 25, 30],
       [33, 65, 35, 4, 69, 70, 7, 37, 9, 42, 10, 41, 14, 50, 51, 84, 60, 29],
       [33, 2, 67, 34, 4, 40, 11, 45, 47, 15, 79, 19, 52, 21, 55, 57, 25],
       [34, 35, 3, 5, 70, 8, 42, 75, 45, 17, 87, 24, 60, 29, 31],
       [4, 41, 11, 76, 44, 45, 16, 83, 53, 29],
       [34, 2, 4, 37, 38, 48, 81, 82, 55, 54, 87, 86, 26, 61, 30],
       [1, 10, 15, 19, 20, 26, 27, 29, 31, 36, 39, 44, 46, 55, 56, 61, 79, 84, 87]]

u_3 = list(range(1, 31))

c_4 = [[2, 4, 6], [8, 10, 12], [14, 16, 18], [20, 22, 24], [26, 28, 30],
       [1, 2],
       [3, 4],
       [5, 6],
       [7, 8],
       [9, 10],
       [11, 12],
       [13, 14],
       [15, 16],
       [17, 18],
       [19, 20],
       [21, 22],
       [23, 24],
       [25, 26],
       [27, 28],
       [29, 30],
       ]

c_5 = [[7, 73, 9, 75, 11, 48, 82, 23],
       [65, 4, 6, 43, 44, 76, 14, 79, 50, 83, 52, 60, 30, 63],
       [1, 2, 3, 13, 14, 21, 28, 31, 40, 44, 49,
           54, 62, 67, 70, 72, 76, 78, 83, 85],
       [0, 4, 14, 15, 17, 20, 22, 27, 40, 43, 59,
           60, 61, 62, 63, 64, 66, 73, 77, 80],
       [0, 68, 8, 11, 14, 57],
       [64, 65, 34, 4, 39, 41, 75, 76, 46, 80, 52, 22, 23, 62],
       [68, 71, 9, 77, 13, 46, 53, 24, 56, 28, 29],
       [66, 67, 74, 42, 79, 18, 52, 21, 23, 25, 27, 61, 57],
       [64, 2, 35, 37, 10, 79, 81, 82, 51, 19, 54, 24, 26, 63],
       [65, 2, 34, 4, 68, 69, 43, 76, 13, 46, 47, 44, 81, 23, 27, 60, 61, 63],
       [3, 5, 11, 14, 21, 22, 24, 25, 26, 27, 32, 35, 38, 44, 58, 59, 69, 76, 84],
       [0, 70, 39, 7, 10, 11, 80, 57, 28, 29, 31],
       [13, 16, 20, 22, 23, 33, 36, 41, 44, 58,
           59, 61, 64, 65, 69, 75, 77, 84, 86],
       [26, 75],
       [41, 12, 47, 48, 18, 87, 25],
       [33, 1, 5, 43, 79, 80, 15, 82, 20, 85, 58, 59, 28, 63],
       [0, 2, 3, 10, 22, 25, 36, 37, 40, 42, 45,
           52, 55, 60, 68, 69, 70, 72, 84, 86],
       [66, 53, 62],
       [65, 34, 68, 27, 43, 44, 46, 16, 49, 50, 19, 55, 21, 87, 24, 25, 59, 29],
       [6, 72, 40, 76, 79, 81],
       [64, 67, 4, 7, 9, 73, 44, 77, 16, 80, 83, 55, 26, 29],
       [39, 43, 45, 78, 15, 79, 47, 18, 86, 23, 59, 31],
       [32, 65, 68, 17, 52, 24, 59, 61]]

solution_1_brute_force = [0, 3, 4, 8, 11, 12, 14, 20, 23] 

solution_2_brute_force = [0, 1, 2, 3, 4, 5, 7, 11, 14, 17] 

solution_3_brute_force = [1, 3, 5, 7, 8, 13, 15, 17, 18, 19, 20, 22, 23] 

solution_4_brute_force = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 

solution_5_brute_force = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16] 

instances = [(u_1, c_1, solution_1_brute_force),
             (u_1, c_2, solution_2_brute_force),
             (u_2, c_3, solution_3_brute_force),
             (u_3, c_4, solution_4_brute_force),
             (u_2, c_5, solution_5_brute_force)]
