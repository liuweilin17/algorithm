###########################################
# Let's Have Some Fun
# File Name: 190.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Oct  4 11:33:02 2018
# 190. Reverse Bits
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            if n <= 0:
                bt = 0
            else:
                bt = n % 2
                n = n/2
            #print bt,
            ret = ret * 2 + bt
            #print ret
        return ret

if __name__=='__main__':
    s = Solution()
    print s.reverseBits(43261596)
