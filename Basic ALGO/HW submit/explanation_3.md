# Search in a Rotated Sorted Array

## Analysis

1. Rearrange Array Elements so as to form two number such that their sum is maximum.
2. The number of digits in both the numbers cannot differ by more than 1.
3. So we need to recursive remove the largest two digits of the array, and plus them to the two number multiply 10.
4. Which algorithem should we choose to sort the arrar?
   Since all the elements is in range 0 to 10,  so it will be really convenient if we use counting sort.

## Complexity

Time complexity is O(N). Counting sort is O(N + R), N is the length of array, R is the size of the counting buckets which is 10. So time complexity is O(N). After sort we traverse array to build two number, this part cost O(N). So the total time complexity is O(N).

Space complexity is O(1). In counting sort we use a extra array sized 10. In the second part, no extra array is used. So the space complexity is O(1).
