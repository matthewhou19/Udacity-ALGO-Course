import math
import random 



def is_sqrt(r, number):
   pow1 = r * r
   pow2 = (r + 1) * (r + 1)
   # r is too large to be sqrt
   if number < pow1 :
      return 1
   # r is too small to be sqrt
   if number >= pow2:
      return -1
   return 0

def sqrt(number):

   """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
   """

   # validation
   if number < 0:
      print("Input must be a nonnagitive integer.")
   left = 0 
   right = number

   while right > left:
      mid = (right + left) // 2
      flag = is_sqrt(mid, number)
      if flag == 0:
         return mid
      elif flag == 1:
         right = mid - 1
      else:
         left = mid + 1
   return left



def sample_test():
   print ("Pass" if  (3 == sqrt(9)) else "Fail")
   print ("Pass" if  (0 == sqrt(0)) else "Fail")
   print ("Pass" if  (4 == sqrt(16)) else "Fail")
   print ("Pass" if  (1 == sqrt(1)) else "Fail")
   print ("Pass" if  (5 == sqrt(27)) else "Fail")

def nagetive_test():
   sqrt(-100)  # Input must be a nonnagitive integer.
   sqrt(-1111) # Input must be a nonnagitive integer.

def random_test():
   print ("Pass" if  (math.isqrt(9) == sqrt(9)) else "Fail")
   for i in range(100):
      num = random.randint(0, 10000)
      print ("Pass" if  (math.isqrt(num) == sqrt(num)) else "Fail")
    

sample_test()
nagetive_test()
random_test()