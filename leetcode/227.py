###########################################
# Let's Have Some Fun
# File Name: 277.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Mar  6 13:38:37 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#227. Basic Calculator II

import re

class Solution:
    # brutal method, not difficult but tedius
    def calculate1(self, s: str) -> int:
        ret = []
        opt_arr = [1]
        for c in s.strip():
            if c == '+':
                opt_arr.append(1)
            if c == '-':
                opt_arr.append(-1)
        arr = re.split('\+|-', s.strip())

        for i in range(len(arr)):
            exp = arr[i].strip()
            var1 = 0
            for j in range(len(exp)):
                if exp[j] == ' ': continue
                elif exp[j] == '*' or exp[j] == '/': break
                else: var1 = var1 * 10 + int(exp[j])
            print(var1)
            print(j)
            opt, var2 = None, 0.1
            for k in range(j, len(exp)):
                if exp[k] == ' ': continue
                elif exp[k] == '*' or exp[k] == '/':
                    if opt == '*' and var2 != 0.1:
                        var1 = var1 * var2
                        var2 = 0.1
                    if opt == '/' and var2 != 0.1:
                        var1 = var1 // var2
                        var2 = 0.1
                    opt = exp[k]
                else: var2 = int(var2) * 10 + int(exp[k])
            if opt == '*' and var2 != 0.1:
                var1 = var1 * var2
            if opt == '/' and var2 != 0.1:
                var1 = var1 // var2

            ret.append(var1 * opt_arr[i])

        return sum(ret)

    # simply use a stack to store the result of sub-expression
    def calculate2(self, s: str) -> int:
        opt = '+'
        num = 0
        st = []
        for i in range(len(s)):
            c = s[i]
            if c >='0' and c<='9':
                num = num * 10 + int(c)

            if c in ['+', '-', '*', '/'] or i == len(s)-1:
                if opt == '+':
                    st.append(num)
                elif opt == '-':
                    st.append(-num)
                elif opt == '*':
                    st.append(st.pop() * num)
                else:
                    tmp = st.pop() #notice the special // in python3 !!!
                    if tmp < 0:
                        st.append(-tmp // num * (-1))
                    else:
                        st.append(tmp // num)
                opt = c
                num = 0
        return sum(st)
