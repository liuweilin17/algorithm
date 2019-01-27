###########################################
# Let's Have Some Fun
# File Name: 49.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 26 10:45:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 49. Group Anagrams

class Solution:
    # my solution, a little redundant
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n < 1: return []

        sorted_strs = sorted(strs, key=lambda x: sorted(x))
        ret = []
        pre = sorted_strs[0]
        tmp = [pre]

        for i in range(1, n):
            cur = sorted_strs[i]
            if sorted(cur) == sorted(pre):
                tmp.append(cur)
            else:
                ret.append(tmp[:])
                tmp = [cur]
            pre = cur

        if tmp:
            ret.append(tmp[:])
        return ret

    # sorted(str) as key, its anagrams are values
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n < 1: return []

        dt = {}
        for s in strs:
            k = tuple(sorted(s))  # strings cannot be key of dict, but tuple
            if k in dt.keys():
                dt[k].append(s)
            else:
                dt[k] = [s]
        return list(dt.values())  # dt.values() is an object, we need to list()


    # use count
    def groupAnagrams3(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n < 1: return []

        dt = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in dt:
                dt[key].append(s)
            else:
                dt[key] = [s]
        return list(dt.values())
