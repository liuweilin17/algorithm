###########################################
# Let's Have Some Fun
# File Name: 648.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 19 19:40:48 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#648. Replace Words

class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.isEnd = False

class Solution:
    def getRoot(self, tnd, word):
        root = ''
        for c in word:
            if tnd.children[ord(c)-ord('a')]:
                tnd = tnd.children[ord(c)-ord('a')]
                root += c
                if tnd.isEnd: #notice!!!, chose the shortest root.
                    break
            else:
                break
        if not tnd.isEnd:
            return word
        else:
            return root

    def replaceWords(self, dict: 'List[str]', sentence: 'str') -> 'str':
        # build Trie Tree
        root = TrieNode()
        for s in dict:
            tmp = root
            for c in s:
                if not tmp.children[ord(c)-ord('a')]:
                    tmp.children[ord(c)-ord('a')] = TrieNode()
                tmp = tmp.children[ord(c)-ord('a')]
            tmp.isEnd = True

        # search in the root
        ret = []
        for word in sentence.split(" "):
            ret.append(self.getRoot(root, word))

        return ' '.join(ret)
