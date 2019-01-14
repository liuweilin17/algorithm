###########################################
# Let's Have Some Fun
# File Name: 28.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 23 01:40:57 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 28. Implement strStr()

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    # use KMP algorithm
    # the KMP could be found in the CLRS P1002
    # it is interesting
    def strStr1(self, haystack, needle):
        """
        use KMP algorithm
        :param haystack:
        :param needle:
        :return:
        """
        m = len(haystack)
        n = len(needle)
        if n <= 0:
            return 0
        elif m <= 0:
            return -1
        else: pass
        prefixArr = self.getPrefixArray(needle)
        print(prefixArr)
        q = 0 # length of matched needle
        for i in range(m):
            print(i, end=',')
            print(q)
            while q > 0 and needle[q] != haystack[i]:
                q = prefixArr[q-1]
            if needle[q] == haystack[i]:
                q += 1
            if q == n:
                return i - q + 1
                #q = prefixArr[q]
        return -1

    # generate prefix array for KMP
    def getPrefixArray(self, str):
        n = len(str)
        ret = [0] * n
        k = 0
        for i in range(1, n):
            while k > 0 and str[k] != str[i]:
                k = ret[k-1]
            if str[k] == str[i]:
                k += 1
            ret[i] = k
        return ret

if __name__ == '__main__':
    s = Solution()
    '''
    print(s.strStr("hello","ll"))
    print(s.strStr1("hello", "ll"))
    print(s.strStr("aaaaa","bba"))
    print(s.strStr1("aaaaa", "bba"))
    '''
    print(s.strStr("mississippi","issip"))
    print(s.strStr1("mississippi", "issip"))
