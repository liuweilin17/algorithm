###########################################
# Let's Have Some Fun
# File Name: 412.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Oct  4 12:40:26 2018
# 412. Fizz Buzz
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append('FizzBuzz')
            elif i % 3 == 0:
                ret.append('Fizz')
            elif i % 5 == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.fizzBuzz(15)


