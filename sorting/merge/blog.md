# Merge Sort

To know the functioning of merge sort, lets consider an array 
arr[8,4,23,42,16,15]

First we check the length of the array and if it's bigger than 1,
we calculate the mid-point


Now, as we already know that merge sort first divides the whole array iteratively into equal halves, unless the atomic values are achieved. 

Here, we see that an array of 6 items is divided into two arrays of size 3 and 3
```
[8,4,23]
[42,16,15]
```

Now, again find that is left index is less than the right index for both arrays, if found yes, then again calculate mid points for both the arrays.

Now, further divide these two arrays into further halves, until the atomic units of the array is reached and further division is not possible.
```
[8,4]
[23]
```

After dividing the array into the smallest units, start merging the elements again based on comparison of size of elements
```
[4,8]
```
```
[4,8,23]
```

Firstly, compare the element for each list and then combine them into another list in a sorted manner.

Finally, do the final merge.