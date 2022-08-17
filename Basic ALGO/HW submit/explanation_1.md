# Finding the Square Root of an Integer

## Analysis

The Square Root  (R) of an integer N, has three properties:

1. N is greater or equal to R squared.
2. N is less than (R + 1) squared.
3. N is greater or equal to R

So the problem could be converted to find an integer  R in the range of 0 to N. R squared must less or equal to N, (R + 1) squared must greater than N.

We can use Binary Search stratege to find that integer in range of 0 to N.


## Complexity

Time complexity is O(log N). Because we use Binary Search to find a number in range 0 to N. In the worst case we need log N operations.

Space complexity is O(1). No extra space.
