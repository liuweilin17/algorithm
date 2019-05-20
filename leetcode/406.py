###########################################
# Let's Have Some Fun
# File Name: 406.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 15 May 10:03:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#406. Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        if not N: return []

        people_sorted = sorted(people, key=lambda x:x[0])
        ret = [None] * N

        for i in range(N):
            person = people_sorted[i]
            ind = -1
            for j in range(N):
                if ret[j] and ret[j][0] != person[0]: # Notice ret[j][0] != person[0]
                    continue
                ind += 1
                if ind == person[1]:
                    ret[j] = person
                    break
        return ret


