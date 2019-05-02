
class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.word_end = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word_end = True        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.word_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return not node.word_end
        

def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # returns true
    print(trie.search("app"))    # returns false
    print(trie.startsWith("app")) # returns true
    trie.insert("appe")
    print(trie.startsWith("app")) # returns true
    print(trie.startsWith("appe")) # returns false

'''
Trie data structure
Insert complexity: O(k), k: key_length
Search complexity: O(k), k: key_length
'''
if __name__ == "__main__":
    main()