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
    def plusOne1(self, digits):
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

    def plusOne2(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            t = digits[i]
            digits[i] = t % 10
            digits[i-1] += t // 10

        if digits[0] > 9:
            t = digits[0]
            digits[0] = t % 10
            digits.insert(0, t // 10)

        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([4,3,2,1]))
