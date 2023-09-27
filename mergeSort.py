import math

def merge_sort(A):
    n = len(A)
    if (n <= 1):
        return A
    midpoint = math.floor(n/2)
    # recurse on halves:
    L = merge_sort(A[0:midpoint])
    R = merge_sort(A[midpoint::])
    # merge halves:
    i, j, k = 0, 0, 0
    while (i < len(L)) and (j < len(R)):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    return A[0:k] + L[i::] + R[j::]
