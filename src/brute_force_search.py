'''Implementation of the brute force search
algorithm for the Set Cover problem.'''

from set_cover import verification_algorithm
from instances import lst_instances
from set_cover import correct_instance
from set_cover import print_instance
import instances
import sys
import time


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
    best_solution = list(range(len(collection)))  # trivial solution
    for subset in power_set:
        if verification_algorithm(universe, collection, subset) and len(subset) < len(best_solution):
            best_solution = subset
    return best_solution


if __name__ == '__main__':
    instance_num = int(sys.argv[1])
    assert instance_num >= 0 and instance_num < len(
        lst_instances), 'The given instance does not exist.'

    (u, c, bf_solution, bf_time) = lst_instances[instance_num]
    assert correct_instance(u, c)
    print_instance(u, c)
    print('\nsaved: ', bf_solution)
    print('elapsed time: ', bf_time, ' secs')

    start = time.time()
    brute_force_solution = brute_force_search(u, c)
    end = time.time()
    elapsed_time = end - start
    print('\n\ncurrent: ', brute_force_solution)
    print('elapsed time: ', elapsed_time, ' secs')
