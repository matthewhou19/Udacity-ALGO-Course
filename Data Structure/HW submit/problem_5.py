
import hashlib
import time
from unittest.mock import sentinel





class Block:
      def calc_hash(self):
            sha = hashlib.sha256()

            data = self.timestamp + self.data + (str(self.previous_hash))

            hash_str = "We are going to encode this string of data!".encode('utf-8')

            sha.update(hash_str)

            return sha.hexdigest()

      def __init__(self, data, previous_hash):
            times = time.time()
            self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(times))
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash()
            self.pre = None
            self.next = None

    
    
      def get_hash(self):
            return self.hash


class Blockchain:

      def __init__(self):
            self.sentinel = Block("0",0)
            self.sentinel.next = self.sentinel
            self.sentinel.pre = self.sentinel
         

      def last_block_time(self):
            if self.sentinel.pre == self.sentinel:
                  print("There is no block!")
                  return None

            last = self.sentinel.pre
            return last.timestamp
         

      def last_block_data(self):
         last = self.sentinel.pre
         return last.data
      def last_block_hash(self):
         if self.sentinel.pre == self.sentinel:
            print("There is no block!")
            return None
         last = self.sentinel.pre
         return last.hash

      def append(self, data):
         last = self.sentinel.pre
         pre_hash = last.get_hash
         new_block = Block(data, pre_hash)
         
         last.next = new_block
         new_block.pre = last
         self.sentinel.pre = new_block
         new_block.next = self.sentinel


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def test_empty():
      bc = Blockchain()

      print(bc.last_block_time())   # There is no block! None
      print(bc.last_block_data())   # 0
      print(bc.last_block_hash())   # There is no block! None



# Test Case 2
def sample_test():
      bc = Blockchain()
      bc.append('a')
      bc.append('b')
      bc.append('c')
      bc.append('d')
      
      print(bc.last_block_time())   # There is no block! None
      print(bc.last_block_data())   # 0
      print(bc.last_block_hash()) 


# Test Case 3
def data_track_test():
      bc = Blockchain()
      for i in range(100):
            bc.append(str(i))
      
      cur = bc.sentinel
      for i in range(100):
            cur = cur.next
            print(cur.data) # should be from 0 to 99





test_empty()
sample_test()
data_track_test()