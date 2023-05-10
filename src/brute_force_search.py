'''Implementation of the brute force search
algorithm for the Set Cover problem.'''

import set_cover


def all_subsets(n: int) -> list:
    '''Returns a list of lists with all
    the subsets of the set = `{1,2,...,n-1}`.'''
    if n == 0:
        return [[]]
    subsets = []
    arr = [False for i in range(n) if True]
    i = 0
    max_size = 2**n
    while len(subsets) < max_size:  # O(2^n)
        if i == n:  # leaf reached
            subset = [j for j in range(len(arr)) if arr[j]]  # O(n)
            subsets.append(subset)
            # backtrack
            while i >= 0:  # O(n)
                i = i - 1
                if arr[i]:
                    arr[i] = False
                    i = i + 1
                    break
        # put 1's until reaching a leaf
        while i != n:  # O(n)
            arr[i] = True
            i = i + 1
    assert len(subsets) == max_size
    return subsets


def brute_force_search(universe: list, collection: list) -> list:
    '''Brute force search to find the minimum cover for the
    `universe`. Returns a boolean list `solution` where `solution[i] = True` 
    if the element of the `collection` S_i must be in the solution.'''
    power_set = all_subsets(len(collection))
    min_cover = len(collection)
    best_solution = list(range(len(collection))) 
    for subset in power_set:
        if set_cover.verification_algorithm(universe, collection, subset) and len(subset) < min_cover:
            best_solution = subset 
    return best_solution


print(brute_force_search(set_cover.u_1, set_cover.c_2))
