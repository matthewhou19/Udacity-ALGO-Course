# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.



from gettext import find
import re


class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.map = dict()
        # Initialize the node with children as before, plus a handler

    def insert(self, word):
        self.map[word] = RouteTrieNode()
        # Insert the node as before
        return

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
    
    def insert_by_root(self, node, list_words, handler) :
        if len(list_words) == 0:
            if node != self.root:
                node.handler = handler
            else: 
                return
        else:
            word = list_words[0]
            list_words.pop(0)
            if word in node.map.keys():
                self.insert_by_root(node.map[word], list_words, handler)
            else:
                node.insert(word)
                self.insert_by_root(node.map[word], list_words, handler)

    def insert(self, list_words, handler):
        self.insert_by_root(self.root, list_words, handler)
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
    
    def find_by_node(self, node, list_words):
        if len(list_words) == 0 :
            return node
        else:
            word = list_words[0]
            list_words.pop(0)
            if word  not in node.map.keys():
                return None
            else:
                return self.find_by_node(node.map[word], list_words)



    def find(self, list_words):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        return self.find_by_node(self.root, list_words)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler = None, not_found_handler = None):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        list = path.split('/')
        count = 0
        for word in list:
            if word == '':
                count += 1
        for i in range(0, count):
            list.remove("")
        return list
        

    def add_handler(self, path, handler):
        list_word = self.split_path(path)
        self.trie.insert(list_word, handler)
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, path):
        list_word = self.split_path(path)
        node = self.trie.find(list_word)
        
        if node == None or node.handler == None:
            return self.not_found_handler
        else:
            return node.handler

        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        return
    


    # Here are some test cases and expected outputs you can use to test your implementation



def test_default():
        # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

def test_empty():
    router = Router("root handler", "not found handler") 

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/////")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' 
    print(router.lookup("/home/about")) # should print 'not found handler' 
    print(router.lookup("/home/about/")) # should print 'not found handler' 
    print(router.lookup("/home/about/me")) # should print 'not found handler' 

def test_not_cover_root():
    router = Router("root handler", "not found handler") 
    router.add_handler("/", "about handler")

    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/////")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' 
    print(router.lookup("/home/about")) # should print 'not found handler' 
    print(router.lookup("/home/about/")) # should print 'not found handler' 
    print(router.lookup("/home/about/me")) # should print 'not found handler' 

    router.add_handler("///", "about handler")

    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/////")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' 
    print(router.lookup("/home/about")) # should print 'not found handler' 
    print(router.lookup("/home/about/")) # should print 'not found handler' 
    print(router.lookup("/home/about/me")) # should print 'not found handler' 



test_default()
test_empty()
test_not_cover_root()
