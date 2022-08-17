# Search in a Rotated Sorted Array

## Analysis

1. We can divide the rotated array by the middle. Then we got two array A1 and A2.
2. There will be at most one rotated array in this two array. And it is easily to find out which one is sorted array, so the other one shall be in the retated one.
3. It is also very easy to find out if the target number could be in the sorted array by compare the target number to the head and the end of the sorted array.
4. If the target number can be the sorted array, then we can discard the rotated array. Otherwise we dicard the sorted array.
5. That means in every recusive process of 1 to 4, we can dicard half of the remaining array. That is obviously a binary search algorithm, and the time complexity would be O(log N)

## Complexity

As we talked about, time complexity is O(log N).

Space complexity is O(1).
