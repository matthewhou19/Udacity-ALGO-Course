import sys
import heapq
import random

class Node:
    def __init__(self, count, char = None):
        self.count = count
        self.char = char
        self.left = None
        self.right = None
    
    def get_count(self):
        return self.count
    
    def get_char(self):
        return self.char

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __lt__(self, other):
        return self.count < other.count


def dfs_traverse(code, map, node) :
    if node.get_char():
        map[node.get_char()] = code
    else :
        dfs_traverse(code + '0', map, node.left)
        dfs_traverse(code + '1', map, node.right) 



def huffman_encoding(data):

    # special case
    if data == None:
        return None, None
    if len(data) == 0:
        return '0', None


    # build count map
    count_map = dict()
    for char in data:
        if char in count_map:
            count_map[char] = count_map[char] + 1
        else:
            count_map[char] = 1
    
    # build huffman tree
    pq = []
    for char in count_map:
        pq.append(Node(count_map[char], char))
    
    heapq.heapify(pq)

    while len(pq) > 1:
        min1 = heapq.heappop(pq)
        min2 = heapq.heappop(pq)

        sum = Node(min1.get_count() + min2.get_count())
        sum.set_left(min1)
        sum.set_right(min2)
        heapq.heappush(pq, sum)
    
    # build huffman code map
    tree_root = heapq.heappop(pq)
    huffman_map = dict()

    if len(count_map) == 1 :
        huffman_map[tree_root.get_char()] = '0'
    else:
        dfs_traverse('', huffman_map, tree_root)

     
    encoded_data = ""
    for char in data:
        encoded_data = encoded_data + huffman_map[char]

    return encoded_data, tree_root

def find(index, cache, tree):
    if tree.get_char():
        return tree.get_char()
    if index == len(cache) :
        return None
    if cache[index] == '1':
        return find(index + 1, cache, tree.right)
    else : 
        return find(index + 1, cache, tree.left)



def huffman_decoding(data,tree):
    if data == None:
        return None
    if tree == None:
        return ""

    
    huffman_code_map = dict()
    cache = ''
    decoded_data = ""

    for bit in data:
        cache = cache + bit
        char = ''
        if cache not in huffman_code_map:
            char = find(0, cache, tree)
        else:
            char = huffman_code_map[cache]
        
        huffman_code_map[cache] = char
        if char :
            decoded_data = decoded_data + char
            cache = ''
    return decoded_data



# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def test_empty():
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print(decoded_data == a_great_sentence)




# Test Case 2
def test_sample():
    a_great_sentence = "abbcccddddeeeeeffffff"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print(decoded_data == a_great_sentence)




# Test Case 3
def test_random():
    chars = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    a_great_sentence = ""
    
    for i in range(100):
        a_great_sentence = a_great_sentence + chars[random.randrange(27)]

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print(decoded_data == a_great_sentence)





if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print(decoded_data == a_great_sentence)

    test_empty()
    test_sample()
    test_random()