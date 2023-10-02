import numpy as np
import math

def partition(A):
    n = len(A)
    x = A[n-1]
    i = -1
    for j in range(0,n-1):
        if (A[j] <= x):
            i += 1
            A[i],A[j] = A[j], A[i]
    A[i+1], A[n-1] = A[n-1], A[i+1]
    return i+1

def quick_sort(A):
    n = len(A)
    if (n <= 1):
        return A
    q = partition(A)
    L = quick_sort(A[0:q])
    H = quick_sort(A[q+1:n])
    return L + [A[q]] + H