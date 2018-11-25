###########################################
# Let's Have Some Fun
# File Name: 204.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 25 00:34:27 2018
###########################################
#coding=utf-8
#!/usr/bin/python
#204. Count Primes

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True] * n
        if n < 2:
            return 0
        primes[0] = False
        primes[1] = False
        t = int(n ** 0.5) + 1 # notice!!!
        for i in range(2, t):
            if primes[i] == True:
                for j in range(2*i,n,i):
                    primes[j] = False
        return sum(primes)

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
    print(s.countPrimes(4))
