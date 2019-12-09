###########################################
# Let's Have Some Fun
# File Name: 642.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Dec  9 13:11:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#642. Design Search Autocomplete System

import heapq

class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.times = 0
        self.sentence = ""

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        # create Trie Tree
        N = len(sentences)
        for i in range(N):
            self.insert(self.root, sentences[i], times[i])
        self.cur_sen = ""

    def insert(self, nd, s, t):
        for c in s:
            ind = 26 if c == " " else ord(c) - ord('a')
            if nd.children[ind] == None:
                nd.children[ind] = TrieNode()
            nd = nd.children[ind]
        nd.times += t
        nd.sentence = s

    def traverse(self, ret, s):
        nd = self.root
        for c in s:
            ind = 26 if c == " " else ord(c) - ord('a')
            if not nd.children[ind]:
                return []
            else:
                nd = nd.children[ind]
        self.preorder(ret, nd)
        return ret

    def preorder(self, ret, nd):
        if nd.times != 0:
            ret.append((nd.times, nd.sentence))
        for child in nd.children:
            if child: # this is essentail else could be TLE
                self.preorder(ret, child)

    def input(self, c: str) -> List[str]:
        ret = []
        if c != '#':
            self.cur_sen += c
            self.traverse(ret, self.cur_sen)
            ret = heapq.nsmallest(3, ret, lambda x:(-x[0], x[1]))
        else:
            self.insert(self.root, self.cur_sen, 1)
            self.cur_sen = ""
        return [e[1] for e in ret[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
