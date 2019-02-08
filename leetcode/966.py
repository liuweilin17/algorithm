###########################################
# Let's Have Some Fun
# File Name: 966.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec 30 09:56:45 2018
###########################################
#coding=utf-8
#!/usr/bin/python
class Solution:
    def devowel(self, s):
        return ''.join(['*' if c in 'aeiou' else c for c in s])

    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        ret = []
        words_perfect = set(wordlist)
        words_cap = {}
        words_vowel = {}
        for word in wordlist:
            words_cap.setdefault(word.lower(), word)
            words_vowel.setdefault(self.devowel(word.lower()), word)
        
        for query in queries:
            if query in words_perfect:
                ret.append(query)
            elif query.lower() in words_cap.keys():
                ret.append(words_cap[query.lower()])
            elif self.devowel(query.lower()) in words_vowel.keys():
                ret.append(words_vowel[self.devowel(query.lower())])
            else:
                ret.append("")
        return ret
