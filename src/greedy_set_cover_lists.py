'''Implementation of the greedy approximation algorithm for 
the Set Cover problem using lists.'''

from set_cover import correct_instance
from set_cover import verification_algorithm
from set_cover import print_instance
from instances import lst_instances
import sys
import time


def diff(set1: list, set2: list) -> None:  # O(|s2|*|s1|)
    '''Computes the difference between two lists `l1` and 
    `l2` by performing the operation `l1`-`l2` on the list `l1`.'''
    for elem in set2:  # O(|s2|)
        try:
            set1.remove(elem)  # O(|s1|)
        except Exception:
            pass


def elements_covered(set1: list, set2: list) -> int:  # O(|s2|*|s1|)
    '''Calculates the number of elements in `set2` that 
    are contained in `set1`, or in other words, it calculates 
    the number of elements that `set2` covers in `set1`.'''
    covered_elems = 0
    for e in set2:  # O(|s2|)
        if e in set1:  # O(|s1|)
            covered_elems = covered_elems + 1
    return covered_elems


def maximize_uncovered(uncovered_elems: list, subsets: list) -> int:  # O(m*n^2)
    '''Returns the index of the subset in the given list 
    `subsets` that covers the maximum number of
    elements from the list `uncovered_elems`.'''
    i_max = 0
    max_covered_elems = 0
    for i in range(len(subsets)):  # O(m)
        s_i_covered = elements_covered(uncovered_elems, subsets[i])  # O(n^2)
        if s_i_covered > max_covered_elems:
            max_covered_elems = s_i_covered
            i_max = i
    return i_max


def greedy_set_cover(universe: list, collection: list) -> list:
    '''Assuming the input instance is correct, it returns 
    a list with the indices of the subsets that form a 
    cover for the universe.'''
    uncovered_elems = list(universe)  # O(n)
    indexes = []
    while uncovered_elems != []:  # O(m)
        i_max = maximize_uncovered(uncovered_elems, collection)  # O(m*n^2)
        indexes.append(i_max)  # O(1)
        diff(uncovered_elems, collection[i_max])  # O(n^2)
    return indexes


if __name__ == '__main__':
    instance_num = int(sys.argv[1])
    assert instance_num >= 0 and instance_num < len(
        lst_instances), 'The given instance does not exist.'

    (u, c, bf_solution) = lst_instances[instance_num]
    assert correct_instance(u, c)
    assert verification_algorithm(u, c, bf_solution)

    print_instance(u, c)
    start = time.time()
    greedy_solution = greedy_set_cover(u, c)
    end = time.time()
    elapsed_time = end - start

    assert verification_algorithm(u, c, greedy_solution)
    assert verification_algorithm(u, c, bf_solution)

    print('\n\nGreedy set cover solution:')
    print(greedy_solution, end=', ')
    print('size: ' + str(len(greedy_solution)))
    print('elapsed time: ', elapsed_time, ' secs')
    print('\nBrute force solution:')
    print(bf_solution, end=', ')
    print('size: ' + str(len(bf_solution)))
