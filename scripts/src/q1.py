import numpy as np

'''    
    Union of two arrays
    Write a function which returns the union of two sorted arrays. The resulting array should stay sorted.
    Example:
    Input: Array A [5, 7, 8, 10, 15], Array B [2, 5, 7, 9, 12]
    Output: Array C [2, 5, 7, 8, 9, 10, 12, 15]
'''


def uniao_arrays(A, B):
    """ Parameters
        ----------
        A: list
            List of numbers that could be sorted or not. Duplicates allowed.
        B: list
            List of numbers that could be sorted or not. Duplicates allowed.

        Returns
        --------
        C: list
            Sorted and concatenated list which has no duplicates.
    """

    # convert type from list or tuple to numpy array
    arrA = np.array(A)
    arrB = np.array(B)

    # grants sorted arrays
    arrA = np.sort(arrA)
    arrB = np.sort(arrB)

    # concatenate arrays A and B into a union array C
    arrC = np.concatenate([arrA, arrB])

    # sorts array C
    sortedC = np.sort(arrC)
    
    # remove duplicates
    sortedC = np.unique(sortedC)

    # changes type to list and returns
    C = sortedC.tolist()
    return C


if __name__ == '__main__':
    A = [5, 7, 8, 10, 15]
    B = [2, 5, 7, 9, 12]
    C = uniao_arrays(A, B)
    print(C)
