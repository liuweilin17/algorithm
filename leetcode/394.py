###########################################
# Let's Have Some Fun
# File Name: 394.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon May 20 14:22:59 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c != ']':
                st.append(c)
            else:
                rep_body = ''
                while st[-1] != '[':
                    rep_body = st.pop() + rep_body
                if st and st[-1] == '[':
                    st.pop() # pop '['
                    rep_num = ''
                    while st and st[-1].isdigit():
                        rep_num = st.pop() + rep_num
                    t = int(rep_num) * rep_body
                    for tt in t:
                        st.append(tt)

        return ''.join(st)


