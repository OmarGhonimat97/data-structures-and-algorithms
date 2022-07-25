
[8,4,23,42,16,15]

### First Pass:
Initially, the first two elements of the array are compared in insertion sort.
[***8***,***4***,23,42,16,15] >> [4,8,23,42,16,15]



Here, 8 is greater than 4 hence they are not in the ascending order and 8 is not at its correct position.
Thus, swap 4 and 8.

### Second Pass:

Now, move to the next two elements and compare them.

[4,***8***,***23***,42,16,15] >> [4,8,23,42,16,15]

Here, 23 is greater than 8, thus both elements seems to be in ascending order, hence, no swapping will occur.
8 also stored in a sorted sub-array along with 4


### Third Pass:

Now, two elements are present in the sorted sub-array which are 4 and 8.

Moving forward to the next two elements which are 23 and 42

[4,8,***23***,***42***,16,15] >> [4,8,23,42,16,15]

Here, 42 is greater than 23, thus both elements seems to be in ascending order, hence, no swapping will occur.

### Fourth Pass:

Now, three elements are present in the sorted sub-array which are 4, 8 and 23.

[4,8,23,***42***,***16***,15]

Both 42 and 16 are not present at their correct place so swap them

[4,8,23,***16***,***42***,15]

After swapping, elements 23 and 16 are not sorted, thus swap again

[4,8,***16***,***23***,42,15]

### Fifth Pass:

Now, the elements which are present in the sorted sub-array are 4, 8, 16 and 23

Moving forward to the next two elements which are 42 and 15

[4,8,16,23,***42***,***15***]

Both 42 and 16 are not present at their correct place so swap them

[4,8,16,23,***15***,***42***]

After swapping, elements 23 and 15 are not sorted, thus swap again

[4,8,16,***15***,***23***,42]

Here, also swapping makes 16 and 15 unsorted hence, swap again

[4,8,***15***,***16***,23,42]

Finally, the array is completely sorted.









