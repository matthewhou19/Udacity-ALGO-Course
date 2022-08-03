# Problem 5 : Blockchain

## Problem Analyzing

1. Everytime we want add a new block to the blockchain , we add it at the end. So we must track the last block.
2. We may want to traverse the blockchain from the start, So we can also track the first block

## Complexity

Time complexity for append operation would be O(1), because insert a node in a Deque cost O(1)

Space complexity is O(N), because we need N node to store the data.
