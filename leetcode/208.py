###########################################
# Let's Have Some Fun
# File Name: 208.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 18 21:07:39 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        rt = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if not rt.children[ind]:
                rt.children[ind] = TrieNode()
            rt = rt.children[ind]
        rt.isEnd = True


    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        rt = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if not rt.children[ind]:
                return False
            rt = rt.children[ind]

        return rt != None and rt.isEnd


    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        rt = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if not rt.children[ind]:
                return False
            rt = rt.children[ind]

        return rt != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
