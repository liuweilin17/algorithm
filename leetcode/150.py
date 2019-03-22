###########################################
# Let's Have Some Fun
# File Name: 150.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Mar  7 14:32:35 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                st.append(st.pop() + st.pop())
            elif t == "-":
                st.append(-st.pop()+st.pop())
            elif t == "*":
                st.append(st.pop() * st.pop())
            elif t == "/":
                st.append(int(1/st.pop() * st.pop()))
            else:
                st.append(int(t))
        return st[0]

