# Problem 6 :Union and Intersection of Two Linked Lists

## Problem Analyzing

### Union

1. sample idea : we can use a set track all the value in the two linked list. But how should we treat the duplicate value in a single linked list?
2. If a value appears in list1 once , appears in list2 twice. Then this value should appears in the union twice.
3. We can use hashmap to store the value as key,  appearence times as value.
4. The time of appearence of each value should be largest one of the  time of appearence in two list


### Intersection

1. Like union function, We can use hashmap to store the value as key,  appearence times as value.
2. The time of appearence of each value should be smallest one of the  time of appearence in two list


## Complexity

### Union

Time complexity is O(N) since we track the two list.

Space complexity is O(N) because we use a dict to store data, in the worst case we would put every value in the dict as a key.


### Intersection

Just like the Union function：

Time complexity is O(N)

Space complexity is O(N)
