###########################################
# Let's Have Some Fun
# File Name: 676.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 19 20:43:16 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#676. Implement Magic Dictionary

class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.isEnd = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()



    def buildDict(self, dict: 'List[str]') -> 'None':
        """
        Build a dictionary through a list of words
        """
        for s in dict:
            rt = self.root
            for c in s:
                if not rt.children[ord(c)-ord('a')]:
                    rt.children[ord(c)-ord('a')] = TrieNode()
                rt = rt.children[ord(c)-ord('a')]
            rt.isEnd = True


    def search(self, word: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        isOneDifferent = False # if we have encountered a different char
        return self.match(word, 0, self.root, isOneDifferent)

    def match(self, word, k, tnd, isOneDifferent):
        if not tnd: return False

        if k == len(word): # reach the end of the word
            if tnd.isEnd and isOneDifferent:
                return True
            else:
                return False

        c = word[k]

        # if isOneDifferent, we have to match the rest of the chars
        if isOneDifferent:
            if tnd.children[ord(c)-ord('a')]:
                return self.match(word, k+1, tnd.children[ord(c)-ord('a')], isOneDifferent)
            else:
                return False

        # if no isOneDifferent, we can match the next char with the same isOneDifferent, or we can mismatch the next char with the isOneDifferent as True
        else:
            for i in range(len(tnd.children)):
                if i == ord(c) - ord('a') and self.match(word, k+1, tnd.children[i], isOneDifferent):
                    return True
                if i != ord(c) - ord('a') and tnd.children[i] and self.match(word, k+1, tnd.children[i], not isOneDifferent):
                    return True
            return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
