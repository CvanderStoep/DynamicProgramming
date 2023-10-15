# Returns the number of arrangements to form the number N
# Given 3 numbers {1, 3, 5}, The task is to tell the total number of ways we can form a number N
# using the sum of the given three numbers. (allowing repetitions and different arrangements)

from functools import lru_cache
from timer_wrapper_functions import timer_func


@timer_func
def recursion(n):
    """
    wrapper function for the solve recursion function
    this is done to be able to time the result using the @timer_func wrapper
    """
    return solve_recursion(n)


#@lru_cache  # use the caching mode to simulate memoization similar to the code in solve_memoization
def solve_recursion(n):
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    return (solve_recursion(n - 1) +
            solve_recursion(n - 3) +
            solve_recursion(n - 5))


@timer_func
def memoization(n):
    """
    wrapper function for the solve memoization function
    this is done to be able to time the result using the @timer_func wrapper
    """

    return solve_memoization(n)


def solve_memoization(n, lookup={}):
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    if n not in lookup:
        lookup[n] = (solve_memoization(n - 1) +
                     solve_memoization(n - 3) +
                     solve_memoization(n - 5))

    return lookup[n]


if __name__ == '__main__':
    print(f'{recursion(n=37)= :,d}')  # with n=37 it already takes >10 seconds
    print(f'{memoization(n=100)= :,d}')  # no problems to increase this

