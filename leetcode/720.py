###########################################
# Let's Have Some Fun
# File Name: 720.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb 20 11:03:33 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#720. Longest Word in Dictionary

class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.isEnd = False

class Solution:
    def longestWord(self, words: 'List[str]') -> 'str':
        ret = ''
        words_sort = sorted(words, key=lambda x:(-len(x), x), reverse=True)
        #print(words_sort)
        # build Trie
        root = TrieNode()
        for word in words_sort:
            tmp = root
            flag = True
            for i in range(len(word)):
                c = word[i]
                if not tmp.children[ord(c)-ord('a')]:
                    tmp.children[ord(c)-ord('a')] = TrieNode()
                    if i != len(word)-1: # notice !!!
                        flag = False
                elif not tmp.children[ord(c)-ord('a')].isEnd:
                    flag = False
                tmp = tmp.children[ord(c)-ord('a')]
            if flag:
                ret = word
            tmp.isEnd = True

        return ret

