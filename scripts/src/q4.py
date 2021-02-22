"""
Smallest number not present

    Given an array A, return the smallest number that is not present. If not, return the
highest number + 1.
Example:
Entry: [1, 7, 5, 2, 3, 20, 4]
Output: 6 (numbers not present in the sequence from 1 to 20: 6, 8, 9, ..., 19)
Entry: [8, 5, 7, 1, 2, 4, 6]
Output: 3
Entry: [3, 5, 2, 1, 4, 6, 7]
Output: 8
"""


def min_not_present(A):
    A.sort()
    list_not_presents = [i for i in range(A[0], A[-1] + 1) if i not in A]
    try:
        minimum = min(list_not_presents)
        return minimum
    except ValueError:
        return max(A) + 1


if __name__ == '__main__':
    A = [1, 7, 5, 2, 3, 20, 4]
    o = min_not_present(A)
    print(o)

    A = [8, 5, 7, 1, 2, 4, 6]
    o = min_not_present(A)
    print(o)

    A = [3, 5, 2, 1, 4, 6, 7]
    o = min_not_present(A)
    print(o)
