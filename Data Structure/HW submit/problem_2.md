# Problem 2 : File Recursion

## Problem Analyzing

### Requirments

1. input: suffix(str): suffix if the file name to be found , path(str): path of the file system
2. output : a list of paths

### Analyzing

1. Obviously this problem can be solved by using recursion programming.
2. Noticed that "There are no limit to the depth of the subdirectories can be." , if we implement a recursive function , stack overflow may occur. So we can use a external stack to replace the role of the system call stack



## Complexity

### Time Complexity

Time complexity is O(N) , because we traversed all the directories and files

### Space Complexity

Space compexity is O(N) , because in the worst case , all files and  directories is in  the orignal path,  then the size of the stack would be almost the total number of the directories and files.
