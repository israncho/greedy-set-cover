'''Implementation of the greedy approximation algorithm for 
the Set Cover problem using lists.'''

import set_cover


def diff(l1: list, l2: list) -> None:
    '''Computes the difference between two lists `l1` and 
    `l2` by performing the operation `l1`-`l2` on the list `l1`.'''
    for elem in l2:
        try:
            l1.remove(elem)
        except Exception:
            pass


def elements_covered(set1: list, set2: list) -> int:
    '''Calculates the number of elements in `set2` that 
    are contained in `set1`, or in other words, it calculates 
    the number of elements that `set2` covers in `set1`.'''
    covered_elems = 0
    for e in set2:
        if e in set1:
            covered_elems = covered_elems + 1
    return covered_elems


def maximize_uncovered(uncovered_elems: list, subsets: list) -> int:
    '''Returns the index of the subset in the given list 
    `subsets` that covers the maximum number of
    elements from the list `uncovered_elems`.'''
    i_max = 0
    max_covered_elems = 0
    for i in range(len(subsets)):
        s_i_covered = elements_covered(uncovered_elems, subsets[i])
        if s_i_covered > max_covered_elems:
            max_covered_elems = s_i_covered
            i_max = i
    return i_max


def greedy_set_cover(universe: list, collection: list) -> list:
    '''Assuming the input instance is correct, it returns 
    a list with the indices of the subsets that form a 
    cover for the universe.'''
    uncovered_elems = list(universe)
    indexes = []
    while uncovered_elems != []:
        i_max = maximize_uncovered(uncovered_elems, collection)
        indexes.append(i_max)
        diff(uncovered_elems, collection[i_max])
    return indexes


print(greedy_set_cover(set_cover.u_1, set_cover.c_1))
