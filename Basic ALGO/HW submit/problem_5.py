#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:



def insert_by_node(node, word):
        if len(word) == 0:
            node.exist = True
        elif word[0] in node.map.keys():
            insert_by_node(node.map[word[0]], word[1:])
        else:
            node.insert(word[0])
            insert_by_node(node.map[word[0]], word[1:])
            
def find_by_node(node, prefix):
        if len(prefix) == 0:
            return node
        elif prefix[0] in node.map.keys():
            return find_by_node(node.map[prefix[0]], prefix[1:])
        else:
            return None
## Represents a single node in the Trie
class TrieNode:
   
    def __init__(self):
        ## Initialize this node in the Trie
        self.exist = False
        self.map = dict()
    
    def insert(self, char):
        self.map[char] = TrieNode()
        ## Add a child node in this Trie
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    
    def insert(self, word):
        insert_by_node(self.root, word)
        ## Add a word to the Trie
    
    
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        return find_by_node(self.root, prefix)


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.exist = False
        self.map = dict()
    def insert(self, char):
        self.map[char] = TrieNode()
        ## Add a child node in this Trie
    def suffixes(self, suffix = ''):
        list = []
        if self.exist == True:
            list.append(suffix)
        for key in self.map.keys():
            list_child = self.map[key].suffixes(suffix + key)
            for word in list_child:
                list.append(word)
        return list
        ## Recursive function that collects the suffix for 
        ## all complete words below this point


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[3]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[4]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');

