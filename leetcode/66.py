###########################################
# Let's Have Some Fun
# File Name: 66.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Nov 14 18:11:38 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#66. Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        sum = 0
        for i in range(l):
            sum = sum * 10 + digits[i]
        sum += 1
        ret = []
        #print(sum)
        while sum > 0:
            tmp = sum % 10
            ret.append(int(tmp))
            sum = int(sum / 10)
        #print(len(ret))
        ret.reverse()
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([4,3,2,1]))
