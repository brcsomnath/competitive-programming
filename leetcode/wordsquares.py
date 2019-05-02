class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.word_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word_end = True

    def search(self, prefix):
        node = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node

def word_squares(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    ans = []
    for word in words:
        square = []
        square.append(word)
        solution(word, trie, len(word), ans)

def solution(square, trie, length, ans):
    if len(square) == length:
        ans.append(square)
        return
    
    prefix = get_prefix(square)
    node = trie.search(prefix)
    if node is None:
        return
    
    children = []
    get_children(node, prefix, children)
    for c in children:
        if len(c) != length:
            continue
        square.append(c)
        solution(square, trie, length, ans)
        square = square[:-1]
    

def get_children(node, prefix, children):
    if node.word_end:
        children.append(prefix)
        return
    
    for i in range(26):
        if node.children[i] is not None:
            get_children(node.children[i], prefix + chr(ord('a')+i), children)


def get_prefix(square):
    idx = len(square)
    prefix = ""
    for w in square:
        prefix += w[idx]
    return prefix