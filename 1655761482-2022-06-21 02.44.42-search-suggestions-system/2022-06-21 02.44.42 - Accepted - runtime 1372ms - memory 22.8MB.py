from queue import PriorityQueue

class Node:
    def __init__(self, c=''):
        self.char = c
        self.end = False
        self.children = {}
    
class Trie:
    def __init__(self, words):
        self.root = Node()
        self.found = 0
        for word in words:
            self.insert(word)
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = Node(w)
                node = node.children[w]
        
        node.end = True
    
    def startsWith(self, pre):
        node = self.root
        for w in pre:
            if w in node.children:
                node = node.children[w]
            else:
                return []
            
        return [pre[:-1] + path for path in self.dfs(node)]
    
    def dfs(self, node):
        self.found = 0
        path = self._dfs(node, '', 0)
        self.found = 0
        return path
    
    def _dfs(self, node, path, cont=0):
        if self.found >= 3:
            return []
        
        if not cont:
            path += node.char            

        if node.end and not cont:
            self.found += 1
            return [path] + self._dfs(node, path, 1)

        keys = sorted(node.children)
        l = []
        for key in keys:
            l += self._dfs(node.children[key], path)
        
        return l
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        return [ trie.startsWith(searchWord[:i]) for i in range(1, len(searchWord)+1) ]
            