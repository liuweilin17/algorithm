###########################################
# Let's Have Some Fun
# File Name: 211.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 19 17:10:47 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#211. Add and Search Word - Data structure design

class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        rt = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if not rt.children[ind]:
                rt.children[ind] = TrieNode()
            rt = rt.children[ind]
        rt.isEnd = True


    def search1(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        rt = self.root
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                flag = False
                for j in range(len(rt.children)):
                    child = rt.children[j]
                    if child:
                        tmp = list(word)
                        tmp[i] = chr(ord('a')+j)
                        if self.search(''.join(tmp)):
                            flag = True
                return flag
            else:
                ind = ord(c) - ord('a')
                if not rt.children[ind]:
                    return False
                rt = rt.children[ind]

        return rt != None and rt.isEnd
    
    def search2(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(list(word), 0, self.root)

    def match(self, wordLst, k, tnd):
        if k == len(wordLst):
            return tnd and tnd.isEnd
        if wordLst[k] != '.':
            return tnd.children[ord(wordLst[k])-ord('a')] != None and \
                    self.match(wordLst, k+1, tnd.children[ord(wordLst[k])-ord('a')])
        else:
            for c in tnd.children:
                if c and self.match(wordLst, k+1, c):
                    return True
            return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
