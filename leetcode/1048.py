###########################################
# Let's Have Some Fun
# File Name: 1048.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun May 19 21:02:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1048. Longest String Chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dt1 = collections.defaultdict(list)
        for word in words:
            n = len(word)
            for i in range(n):
                dt1[word[:i] + '*' + word[i+1:]].append(word)

        dt2 = collections.defaultdict(int)
        words.sort(key=lambda x:len(x), reverse = True)
        ret = 0
        for word in words:
            n = len(word)
            maxL = 0
            for i in range(n+1):
                next_word = word[:i] + '*' + word[i:]
                if next_word in dt1:
                    next_word_list = dt1[next_word]
                    for tmp in next_word_list:
                        maxL = max(maxL, dt2[tmp])
            dt2[word] = maxL + 1
            ret = max(maxL+1, ret)

        return ret

