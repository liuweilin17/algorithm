###########################################
# Let's Have Some Fun
# File Name: 677.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 19 21:04:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#677. Map Sum Pairs

class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.isEnd = False
        self.val = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, key: 'str', val: 'int') -> 'None':
        rt = self.root

        for c in key:
            if not rt.children[ord(c)-ord('a')]:
                rt.children[ord(c)-ord('a')] = TrieNode()
            rt = rt.children[ord(c)-ord('a')]
        rt.isEnd = True
        rt.val = val

    def sum(self, prefix: 'str') -> 'int':
        rt = self.root
        ret = 0
        for c in prefix:
            if rt.children[ord(c)-ord('a')]:
                rt = rt.children[ord(c)-ord('a')]
            else:
                return ret
        return self.count(rt)

    def count(self, rt):
        if not rt: return 0
        ret = 0
        if rt.isEnd: ret += rt.val
        for child in rt.children:
            ret += self.count(child)
        return ret


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
