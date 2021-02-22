"""
    Given an A array, return the most frequent numbers and its respective frequencies.
    Tiebreaker: it is allowed to return any of the tie cases, if occurs.

    Example:
        Input: [1,5,7,3,2,1, 4, 7, 8, 15, 0, 9, 1, 1, 7, 4]
        Output:
        1 -> (4 occurrences)
        7 -> (3 occurrences)
        4 -> (2 occurrences)
"""

import pandas as pd


def top_three(A):
    # converts array to a pandas series
    A_series = pd.Series(A)
    # counts occurrences for all elements
    ranking = A_series.value_counts()
    # returns the first three elements from the head of the series
    return print(ranking.head(3))


if __name__ == '__main__':
    A = [1, 5, 7, 3, 2, 1, 4, 7, 8, 15, 0, 9, 1, 1, 7, 4]
    top_three(A)
