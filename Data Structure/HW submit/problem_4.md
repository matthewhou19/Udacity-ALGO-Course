# Problem 4 : Active Directory

## Problem Analyzing

1. When we look up a group, we may find other groups. That means we will face same structer again and again. So we can implement a dfs ALGO by using recursive strategy.
2. Since we don't  want to check the same groups twice, which can cause finite loop. We can use a set to track all the group we have met before.


## Complexity

Time complexity is O(N) , because in the worst case we need to traverse every group and user.

Space complexity is O(M) , M is the number of groups. In the worst case we need to put every group in the call stack.
