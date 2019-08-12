###########################################
# Let's Have Some Fun
# File Name: 241.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed  3 Jul 23:19:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#241. Different Ways to Add Parentheses

class Solution:
    # the key to solution is dividing the array based on operator !!!!
    def diffWaysToCompute(self, input: str) -> List[int]:
        def calculate(s): # return value given string s
            ret = []
            for i in range(len(s)):
                if s[i] in ['+', '-', '*']:
                    values1 = calculate(s[:i])
                    values2 = calculate(s[i+1:])
                    for v1 in values1:
                        for v2 in values2:
                            if s[i] == '+':
                                ret.append(v1 + v2)
                            elif s[i] == '-':
                                ret.append(v1 - v2)
                            elif s[i] == '*':
                                ret.append(v1 * v2)
                            else: pass
            if not ret: return [int(s)]
            else: return ret

        return calculate(input)



