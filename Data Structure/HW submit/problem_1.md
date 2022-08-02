# Problem 1 : Least Recently Used Cache

## Problem Analyzing

### Requirments

1. get() and put() operation's runtime should be O(1)
2. when the cache size reaches its capacity, remove the Least recently used entry .  remove() operation should also be fast.

### Analyzing

1. Since get() and put() operation should be O(1) and we need  to retrieve the value by the entry, we need use a HashMap to store the data.
2. Since we want to remove the "Least recently used entry", we must use a data structere to remember the order of the element. First used element will go out first.  Seems we can used a Queue here.  But there is acturally a tricky part of problem, when we reuse an element which is already in the Queue, we must "refresh" this element's priority.
3. To refresh the element's  priority ,  we need reorder the queue as we want. To implement this idea we need change the Queue  to a Deque.

## Complexity

### Time Complexity

1. __init()  cost O(1)__
2. get () costO(1). Because get from value from dict cost O(1) ,  change order from Deque cost O(1)
3. set cost  O(1) . Because add a pair in dict cost O(1), add a Node in Deque cost O(1)

### Space Complexity

Space complexity is O（C）,  C is capacity of the LRC  because we need a Deque and a dict both sized C to store data.
