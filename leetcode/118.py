###########################################
# Let's Have Some Fun
# File Name: 118.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov  9 11:44:14 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 118. Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 1
        ret = []
        while i<=numRows:
            cur = [1] * i
            if i>=3:
                pre = ret[i-2]
                for j in range(1,i-1):
                    cur[j] = pre[j-1] + pre[j]
            ret.append(cur)
            i+=1
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
