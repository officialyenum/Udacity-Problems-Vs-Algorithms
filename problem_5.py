
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        self.word_list = []

    def insert(self, word):
        ## Add a word to the Trie
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
                
            current_node = current_node.children[char]

        for a,n in current_node.children.items():
            current_node.setSuffix(current_node.suffix(a))
        
        current_node.is_word = True
    

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in prefix:
            print(current_node.children.get(char))
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word

    def appendWordRecursion(self, node, word, key_length):
        
        # Method to recursively traverse the trie
        # and return a whole word.
        if node.is_word:
            self.word_list.append(word[key_length:])

        for a,n in node.children.items():
            self.appendWordRecursion(n, word + a, key_length)

    def getSuffixList(self, key):
        
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        current_node = self.root
        not_found = False
        temp_word = ''
        key_length = len(key)
        if key == '':
            return []

        for a in list(key):
            if not current_node.children.get(a):
                not_found = True
                break

            temp_word += a
            current_node = current_node.children[a]

        if not_found:
            return 0
        elif current_node.is_word and not current_node.children:
            return -1

        self.appendWordRecursion(current_node, temp_word, key_length)
        
        return self.word_list

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test Case 1
print(MyTrie.getSuffixList("tri")) # returns ['e', 'gger', 'gonometry', 'pod'] list of suffix
# Test Case 2
print(MyTrie.getSuffixList("")) # returns [] cos no prefix was passed as an argument
# Test Case 3
print(MyTrie.getSuffixList("f")) # returns ['e', 'gger', 'gonometry', 'pod', 'un', 'unction', 'actory'] list of suffix
# Test Case 4
print(MyTrie.getSuffixList("tries")) # returns 0 cos it does not exist
# Test Case 5
print(MyTrie.getSuffixList("trie")) # returns -1 cos it is a word