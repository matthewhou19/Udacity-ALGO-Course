


from queue import Queue
import tarfile
from unittest.mock import sentinel


class Node:
    def __init__(self, value, entry = None):
        self.value = value
        self.entry = entry
        self.next = None
        self.pre = None



class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
       
        # in case we get negative input
        self.capacity = max(capacity, 1)
        self.size = 0
        self.map = dict()

        # use sentinal Node can make insert delete to a Deque easily
        self.sentinel = Node(0)
        self.sentinel.next = self.sentinel
        self.sentinel.pre = self.sentinel
    
    def add_head(self, node):
        tail = self.sentinel.next
        node.next= tail
        node.pre = self.sentinel
        self.sentinel.next = node
        tail.pre = node

    # move an exist node to the head(next to the sentinal)
    def move_to_head(self, node):
        left = node.pre
        right = node.next
        
        # remove node from the original position
        left.next = right
        right.pre = left
        node.next = None
        node.pre = None

        self.add_head(node)
        

    def remove_last(self):
        last = self.sentinel.pre
        before = last.pre
        before.next = self.sentinel
        self.sentinel.pre = before

        key = last.entry
        del self.map[key]

        self.size -= 1    
    # USER API
    def get(self, key):
         # Retrieve item from provided key. Return -1 if nonexistent. 

        if key in self.map:
            node = self.map[key]
            self.move_to_head(node)
            return node.value
        return -1
       
        
    #USER API
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.move_to_head(node)
        else:
            if self.size == self.capacity:
               self.remove_last()
               
            else:
                node = Node(value, key)
                self.map[key] = node
                self.add_head(node)
                self.size += 1
            
        
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))   # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
