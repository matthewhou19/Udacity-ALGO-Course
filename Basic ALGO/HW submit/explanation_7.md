# HTTPRouter using a Trie

## Analysis

1. we use map to implement the TrieNode class rather than array.
2. we can broke the path into list of words, and ignore the empty string

## Complexity

1. Insert handler
   Time complexity is O(L) ,L is the length of the path.
   space complexity is O(L). In the worst case we create L new Node.
2. lookup handler
   Time complexity is O(L) ,L is the length of the path
   space complexity is O(1).
