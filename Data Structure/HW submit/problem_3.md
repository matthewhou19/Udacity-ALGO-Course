# Problem 3 : Huffman Coding

## Problem Analyzing

### Encode

It is obvious that the key of the solution is to build a Priority Queue (PQ)to sort the Nodes. Since we need to insert Node to the PQ a lot of times , minHeap would be better than sorting the PQ for a lot of time.

So we  need to build a Node class and let it apply for heapq

### Decode

To reduce runtime , we can created a huffman code map as "cache" so we can avoid to traverse the tree to find a code which has been found before.

## Complexity

### Encode

There are 4 main process in the encode function：

1. Iterate the string to build char_count map , time complexity is O(N), space complexity is O(N)
2. Use minheap to build a huffman tree. In the wost case , all the characters appears once in the original string. Then there will be N node in the pq,  we keep poping out 2 node and add one node in the pq, untill there is only one node in the pq. This process will executed N - 1 times, every time cost O(log N) . So the time complexity is O(N * log N), space complexity is O(N)
3. Build huffman_code map by traverse the original string . For every character, we need no more than H (hight of the huffman tree) operations. In worst case, all the characters appears once in the original string ,  and the huffman tree will have the largest number of node. In this case, the huffman tree is a balanced tree, then H is equal to O(log N) . So the time complexity is O(N * log N). The space complexity is O(N)
4. Build the encoded data , time complexity is O(N) , space complexity if O(N)

The total time complexity is O(N * log N) , space complexity is O(N).

### Decode

For every character in the data, we need no more than H (hight of the huffman tree) operations to get the huffman_code. As we discussed above, this process will cost O(N * log N).

So time complexity is O(N * log N). Space complexity is O(N).
