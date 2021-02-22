"""
    Sum N
    Given an A array and a N number, return True if there are numbers X and Y in the A array such that
    X + Y = N. Otherwise, return False.
    Example:
        Input: [1,2,4,7], 9
        Output: True (2 + 7 = 9)
        Input: [3, 4, 6], 6
        Output: False (3 + 4 = 7, 3 + 6 = 9, 4 + 6 = 10)
"""


def sum_n(A, N):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == N:
                return True
    return False


if __name__ == '__main__':
    A = [1, 2, 4, 7]
    N = 9
    C = sum_n(A, N)
    print(C)

    A = [3,4,6]
    N = 6
    C = sum_n(A,N)
    print(C)