###########################################
# Let's Have Some Fun
# File Name: 14.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 20 18:36:34 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ''
        l1 = len(strs[0])
        l2 = len(strs)
        i = 0
        while i < l1:
            c = strs[0][i]
            flag = True
            for j in range(1, l2):
                if len(strs[j])<=i or strs[j][i] != c:
                    flag = False
                    break
            if flag == False:
                break
            i += 1
        return strs[0][:i]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["dog"]))

