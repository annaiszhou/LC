class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.dic = {}
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self
        for w in word:
        	if w not in node.dic:
        		node.dic[w] = Trie()
        	node = node.dic[w]
        node.end = True

    def prefixnode(self,word):
        node = self
        for w in word:
        	if w not in node.dic:
        		return None
        	node = node.dic[w]
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.prefixnode(word)
        if not node:
        	return False
        else:
        	return True if node.end else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.prefixnode(prefix)
        return bool(node)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#Runtime: 208 ms
#Your runtime beats 60.13 % of python submissions.