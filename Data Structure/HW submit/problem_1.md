# Least Recently Used Cache

## Problem Analyzing

### Requirments

1. get() and put() operation's runtime should be O(1)
2. when the cache size reaches its capacity, remove the Least recently used entry .  remove() operation should also be fast.

### Analyzing

1. Since get() and put() operation should be O(1) and we need  to retrieve the value by the entry, we need use a HashMap to store the data.
2. Since we want to remove the "Least recently used entry", we must use a data structere to remember the order of the element. First used element will go out first.  Seems we can used a Queue here.  But there is acturally a tricky part of problem, when we reuse an element which is already in the Queue, we must "refresh" this element's priority.
3. To refresh the element's  priority ,  we need reorder the queue as we want. To implement this idea we need change the Queue  to a Deque.
