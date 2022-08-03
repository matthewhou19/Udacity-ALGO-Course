from random import sample


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    map1 = dict()
    res = LinkedList()
    # initial llist_1 in map1
    cur_node = llist_1.head
    while cur_node:
        key = cur_node.value
        if key in map1:
            map1[key] = map1[key] + 1
        else :
            map1[key] = 1
        cur_node = cur_node.next
        res.append(key)
    
    cur_node = llist_2.head
    while cur_node:
        key = cur_node.value
        if key not in map1:
            res.append(key)
        elif map1[key] != 1:
            map1[key] -= 1
        else:
            del map1[key]
        cur_node = cur_node.next
    
    return res


def intersection(llist_1, llist_2):
    # Your Solution Here
    map1 = dict()
    
    # initial llist_1 in map1
    cur_node = llist_1.head
    while cur_node:
        key = cur_node.value
        if key in map1:
            map1[key] = map1[key] + 1
        else :
            map1[key] = 1
        cur_node = cur_node.next

    res = LinkedList()

    cur_node = llist_2.head
    while cur_node:
        key = cur_node.value
        if key in map1:
            res.append(key)
            if map1[key] == 1:
               del map1[key]
            else :
                map1[key] -= 1
        cur_node = cur_node.next

    return res
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))



# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def test_empty():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))    # list 2
    print (intersection(linked_list_1,linked_list_2)) # empty

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))   # list3
    print (intersection(linked_list_3,linked_list_4))   # empty



# Test Case 2
def sample_test():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3, 4, 5]
    element_2 = [3, 4, 5, 6, 7, 8, 9]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))    # 1 2 3 4 5 6 7 8 9
    print (intersection(linked_list_1,linked_list_2)) # 3 4 5


# Test Case 3

def duplicate_test():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 4, 5, 5, 4, 3, 3, 4, 5]
    element_2 = [3, 5, 5, 5, 5, 6, 6, 6,6]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))    # 1 2 3 3 4 4 4 5 5 5 5 6 6 6 6 
    print (intersection(linked_list_1,linked_list_2)) # 3 5 5 5

test_empty()
sample_test()
duplicate_test()
