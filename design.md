# Project 1 Design Document

Group Members: Alan Jessup and Xinran Liu

## Overview

This piece of software, written in Python, allows the user to compare the performance of Quick Sort, Merge Sort, and Insertion Sort on input lists of varying sizes and generation procedures.

### Execution Instructions

The main file is `sortTest.py`. It can be executed from the command line with:

```
$python3 sortTest.py <min> <incr> <max> <trials> --optional arguments
```

Where the required inputs are integers for:

- Minimum size of test lists
- Increment with which test list size increases
- Maximum size of test lists
- Number of trials done per list size

And the following optional arguments and options can be used to specify which algorithm and/or list generation procedures to test:

- `--whichsorts` MergeSort QuickSort InsertionSort
- `--generator` Random Ordered Evil

By default, the program will test all three algorithms with randomly generated lists.

A good go-to input is `100 100 900 5`. This should not take more than a few seconds to run, and provides a good look at how the performance of each algorithm varies with list size (see `analysis.md` for more details).

### Notes

A maximum list size of 1000 or more using Evil or Ordered list generation with Quick Sort will result in a "maximum recursion depth exceeded" error, since the maximum recursion depth for Python is 1000, and Ordered and Evil list generation result in a worst-case runtime for Quick Sort. As far as I understand, this is unavoidable, and is just a demonstration of QuickSort's difficulty with worst-case runtime.

## Sorting Algorithms

### Quick Sort

The implementation for Quick Sort is given in the function `quick_sort` in `quickSort.py`.

> ---> explanation of how you implemented quicksort

### Merge Sort

The implementation for Merge Sort is given in the function `merge_sort` in `mergeSort.py`.

It is designed to sort an list by splitting it into a right and left sub-list and recursively sorting those, until a sub-list containing 1 or 0 elements is reached. This results in _log(n)_ recursions.

Then, it merges the sub-lists while retaining their sorted order, by iterating through the right and left lists and comparing each of their values until one of the lists is fully placed and the other can simply be added onto the end.

### Insertion Sort

The implementation for Insertion Sort is given in the function `insertion_sort` in `insertionSort.py`.

This is designed to sort an list by iterating through the list and checking if each value is sorted, i.e. is greater than all prior values. If not, it backtracks through the list and inserts the value in the appropriate position.

To do this, it uses two indices _i, j_ to iterate back and forth through the list. _i_ indexes the outer list and iterates through each list item once, and _j_ indexes the inner loop and, for each iteration of _i_, iterates through list items in `sequence[0:j]` until it finds that `sequence[i]` is greater than or equal to the prior value, and therefore all prior values. It then relocates the item indexed at _i_ to position _j+1_, i.e. the position directly above the greatest value which is less than it.

## Sequence Generation

### Ordered and Random Sequences

The random sequences are generated using pseudo-randomized numbers from the Python Random module, seeded with the default current system time.

Ordered sequences are generated trivially using range().

### Evil Sequences

> ---> explanation of how the generator works and why these sequences cause quicksort to run in Theta(n^2) time