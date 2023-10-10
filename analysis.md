# Project 1 Analysis Document

Group Members: Alan Jessup and Xinran Liu

## Comparison of Sorting Algorithms

### Performance on Random Sequences

When comparing all three sorting algorithms on randomly generated sequences, Quick Sort performs best. It appears to increase steadily at the same rate as Merge Sort, which is in line with their theoretical runtime, since both are _O(n log n)_ runtime algorithms. Insertion Sort, being an _O(n\*n)_ runtime algorithm, increases at a much faster rate as the input size grows.

![Fig 1. Graph comparing each algorithm's performance sorting randomly generated sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/random.png)

### Performance on Ordered Sequences

Insertion Sort and Merge Sort both perform well on ordered sequences, with Insertion Sort performing best on smaller sequences and Merge Sort better on sequences with a size greater than about 6,000 items. Quick Sort performs poorly, at its worst-case runtime of _O(n\*n)_.

![Fig 2. Graph comparing each algorithm's performance sorting ordered sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/ordered.png)

![Fig 3. Graph comparing Merge Sort and Quick Sort's performance sorting large ordered sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/large-ordered.png)

### Performance on Evil Sequences

On evil sequences, Merge Sort performs the best by far, since both Quick Sort and Insertion Sort are running at their theoretical worst-case runtime of _O(n\*n)_.

![Fig 4. Graph comparing each algorithm's performance sorting evil sequences](https://github.com/alanrjes/cs382-project1/blob/master/graphs/evil.png)

### Conclusions on Sorting Algorithm Comparisons

Based on this data, Quick Sort appears to be the best choice for random sequences, but by far the worst choice for ordered and evil sequences. Merge Sort performs well all around, almost as well as Quick Sort on random sequences, and by far the best on evil sequences. Insertion sort performs well specifically on small ordered sequences, but in general is expected to perform poorly on larger data sets due to its _O(n\*n)_ runtime increasing more steeply than the _O(n log n)_ runtime of Merge Sort and Quick Sort.

## Evidence for Evil Generator Runtime

...
