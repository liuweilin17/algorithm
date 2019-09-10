###########################################
# Let's Have Some Fun
# File Name: 319.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep  6 09:47:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#319. Bulb Switcher

import math

class Solution:
    # bulb is on <=> bulb is switched odd times
    # since bulb i is switched when round is the divisor of i
    # bulb i is switched odd times <=> i has odd number of divisors
    # since divisors of i come in pairs
    # bulb i has odd number of divisors <=> i is the square of some number
    # for bulb in {1, 2, ..., n-1}
    # the square number is 1^2, 2^2, ..., (int(sqrt(n))^2), 
    # which is counted as int(sqrt(n))
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
        
