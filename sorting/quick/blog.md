# Quick Sort

Quicksort is a sorting algorithm based on the divide and conquer approach where



Working of Quicksort Algorithm

> Select the Pivot Element

There are different variations of quicksort where the pivot element is selected from different positions. Here, we will be selecting the rightmost element of the array as the pivot element.

> Rearrange the Array

Now the elements of the array are rearranged so that elements that are smaller than the pivot are put on the left and the elements greater than the pivot are put on the right.

Here's how we rearrange the array:

1. A pointer is fixed at the pivot element. The pivot element is compared with the elements beginning from the first index.
2. If the element is greater than the pivot element, a second pointer is set for that element.
3. Now, pivot is compared with other elements. If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.
4. Again, the process is repeated to set the next greater element as the second pointer. And, swap it with another smaller element.
5. The process goes on until the second last element is reached.
6. Finally, the pivot element is swapped with the second pointer.

> Divide Sub-arrays

Pivot elements are again chosen for the left and the right sub-parts separately. And, step 2 is repeated.

The sub arrays are divided until each subarray is formed of a single element. At this point, the array is already sorted.





