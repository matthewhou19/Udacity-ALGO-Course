
import os
def find_files(suffix, path):

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path and suffix:


      stack = []

      res = []

      stack.append(path)

  
      

      
      while len(stack) > 0:
      # case 1: path is a file end with suffix, return the path

      # case 2: path is a file, but not end with suffix, return None

      # case 3: path is a dir, add all the child paths in the stack


        cur = stack.pop()
        if os.path.isdir(cur):
          for dir in os.listdir(cur):
            stack.append(os.path.join(cur, dir))
        elif os.path.isfile(cur):
          if cur.endswith(suffix):
            res.append(cur)





      return res
    return []

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

def default_test():
  files = find_files(".c", "./testdir")
  for file in files:
    print(file)
   
  '''
  ./testdir/t1.c
  ./testdir/subdir5/a.c
  ./testdir/subdir3/subsubdir1/b.c
  ./testdir/subdir1/a.c
  '''

# Test Case 2
def empty_test():
  files = find_files(".a", ".")
  for file in files:
    print(file) 
  
  # will do nothing because files is empty

# Test Case 3
def none_test():
  files = find_files(".a", None)
  for file in files:
    print(file) 
 # will do nothing because files is empty
  

default_test()
empty_test()