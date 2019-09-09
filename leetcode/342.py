###########################################
# Let's Have Some Fun
# File Name: 342.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Sep  7 09:10:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python



class Solution:
    # my solution
    def isPowerOfFour1(self, num: int) -> bool:
        if num <= 0: return False
        i = 0
        flag = True
        exist = False
        while num:
            digit = num & 1
            print(digit, i)
            if digit == 1:
                if i % 2 == 0:
                    if exist == True:
                        flag = False
                        break
                    else:
                        exist = True
                else:
                    flag = False
                    break
            num >>= 1
            i += 1

        return flag

    def isPowerOfFour2(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and \
    num & 0x55555555 == num
