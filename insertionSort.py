def insertion_sort(sequence):
    n = len(sequence)
    i = 0
    while (i < n):
        j = i-1
        while (j >= -1):
            if ((j == -1) or (sequence[j] <= sequence[i])):
                sequence.insert(j+1, sequence.pop(i))
                break
            j -= 1
        i += 1
    return sequence
