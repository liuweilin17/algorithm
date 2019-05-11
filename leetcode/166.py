###########################################
# Let's Have Some Fun
# File Name: 166.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 21:20:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 166. Fraction to Recurring Decimal

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0: return '0'
        
        res = ''
        if numerator * denominator < 0: 
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        res += str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return res
        
        res += '.'
        remains = {}
        remains[numerator] = len(res) # 记录出现的余数，如果有重复余数出现，则开始循环
        while numerator != 0:
            numerator *= 10
            res += str(numerator // denominator)
            numerator %= denominator
            if numerator in remains:
                index = remains[numerator] #res[index] 是循环体里的第一个数
                res = res[:index] + '(' + res[index:] + ')'
                break
            else:
                remains[numerator] = len(res)
                
        return res
            
