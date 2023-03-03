# Returns the number of arrangements to form the number n'
# Given 3 numbers {1, 3, 5}, The task is to tell the total number of ways we can form a number N
# using the sum of the given three numbers. (allowing repetitions and different arrangements)

def solve_recursion(n):
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    return (solve_recursion(n - 1) +
            solve_recursion(n - 3) +
            solve_recursion(n - 5))


def solve_memoization(n, lookup={}):
    # This function returns the number of
    # arrangements to form 'n'

    # lookup dictionary/hashmap is initialized

    # Base cases
    # negative number can't be
    # produced, return 0
    if n < 0:
        return 0

    # 0 can be produced by not
    # taking any number whereas
    # 1 can be produced by just taking 1
    if n == 0:
        return 1

    # Checking if number of way for
    # producing n is already calculated
    # or not if calculated, return that,
    # otherwise calculate and then return
    if n not in lookup:
        lookup[n] = (solve_memoization(n - 1) +
                     solve_memoization(n - 3) +
                     solve_memoization(n - 5))

    return lookup[n]


if __name__ == '__main__':
    print(solve_recursion(20))
    print(solve_memoization(20))
