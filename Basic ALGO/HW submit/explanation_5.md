# Autocomplete with Trie

## Analysis

1. To save space, we use map to implement the TrieNode class rather than array.

## Complexity

1. Insert word
   Time complexity is O(L) ,L is the length of the word.
   space complexity is O(L). In the worst case we create L new Node.
2. find Node by prefix
   Time complexity is O(L) ,L is the length of the prefix
   space complexity is O(1).
3. list all the suffixes
   Time complexity is O(N) , N is the number of Nodes after the one is being called by function.Because we traverse all of them once.
   Space complexity is O(1)
