
# Dutch National Flag Proble

## Analysis

1. Given an input array consisting on only 0, 1, and 2
2. sort the array in a single traversal.
3. Like problem 3 , we cound use counting sort. But counting sort must traverse the array at least twice.
4. So we can use 3 point partition algorithm to saperate the element small than 1, equal to 1, or large than 1.

## Complexity

Time complexty is O(N), because we only traverse the array once.

Space complexity is O(1). No extra space.
