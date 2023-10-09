# Project 1 Analysis Document

Group Members: Alan Jessup and Xinran Liu

## Comparison of Sorting Algorithms

### Performance on Random Sequences

When comparing all three sorting algorithms on randomly generated sequences, Quick Sort performs best. It appears to increase steadily at the same rate as Merge Sort, which is in line with their theoretical runtime, since both are _O(n log n)_ runtime algorithms.

![Fig 1. Graph of all algorithms' performance sorting randomly generated sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig1.png)

A moderate anomaly in the data appears when Merge Sort is compared against Insertion Sort, without running Quick Sort. In this case, Insertion Sort appears to outperform Merge Sort on small sequences, worsening as the input size grows.

![Fig 2. Graph comparing Merge Sort and Insertion Sort's performance sorting randomly generated sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig2.png)

This anomaly may be due to Python's internal optimization processes allowing Merge Sort to benefit from the prior work done by Quick Sort.

### Performance on Ordered Sequences

Similarly to the findings of Merge Sort and Insertion Sort's relative performance on random sequences, Insertion Sort perform best on small sequence sizes, but worse as the sequence size increases. Both Merge Sort and Insertion Sort perform significantly better on ordered sequences than random sequences.

![Fig 3. Graph comparing Merge Sort and Insertion Sort's performance sorting ordered sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig3.png)

Because of Python's recursion depth limit, Quick Sort is not able to complete Ordered or Evil sequences larger than 1,000 items. For sequences of size less than 1,000, Quick Sort completes in its worst-case runtime, and is vastly outperformed by the other two algorithms.

![Fig 4. Graph comparing Quicksort's performance sorting ordered sequences of a limited size](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig4.png)

### Performance on Evil Sequences

Quicksort demonstrates the same worst-case runtime when tested on evil sequences as it does on ordered sequences.

![Fig 5. Graph of all algorithms' performance sorting evil sequences of a limited size](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig5.png)

On larger evil sequences, Merge Sort performs far better than Insertion Sort. This is in line with the theoretical runtime of Insertion Sort, since evil sequences result in Insertion Sort's worst-case runtime of _O(n\*n)_.

![Fig 6. Graph comparing Merge Sort and Insertion Sort's performance sorting evil sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/fig6.png)

### Conclusions on Sorting Algorithm Comparisons

Based on this data, Quick Sort appears to be the best choice for random sequences, but by far the worst choice for ordered and evil sequences. Merge Sort performs well all around, and is the best choice for evil sequences and for large ordered sequences. Insertion sort performs well on small random and ordered sequences, but poorly on larger data sets, since due to its _O(n\*n)_ runtime increases more steeply than the _O(n log n)_ runtime of Merge Sort and Quick Sort.

## Evidence for Evil Generator Runtime

...
