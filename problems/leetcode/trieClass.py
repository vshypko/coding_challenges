# 208
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            charIndex = ord(c) - ord('a')
            if not node.children[charIndex]:
                node.children[charIndex] = TrieNode()
            node = node.children[charIndex]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for i in range(len(word) - 1):
            charIndex = ord(word[i]) - ord('a')
            if not node.children[charIndex]:
                return False
            node = node.children[charIndex]
        lastIndex = ord(word[-1]) - ord('a')
        return node.children[lastIndex] is not None and node.children[lastIndex].isEnd

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            charIndex = ord(c) - ord('a')
            if not node.children[charIndex]:
                return False
            node = node.children[charIndex]
        return True
