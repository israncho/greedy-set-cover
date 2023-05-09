'''Implementation of the brute force search
algorithm for the Set Cover problem.'''


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
    ''''''
    pass


print(all_subsets(3))
