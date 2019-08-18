###########################################
# Let's Have Some Fun
# File Name: 89.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 16 Aug 11:28:34 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#89. Gray Code

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # key: add 0 and 1 to a(grey) and reverse_a(gret)
        def helper(m):
            if m == 1:
                return [0, 1]
            else:
                lst = helper(m-1)
                lst_rev = lst[::-1]
                lst_new = [e * 2 for e in lst]
                lst_rev_new = [e * 2 + 1 for e in lst_rev]
                return lst_new + lst_rev_new

        return [0] if n <= 0 else helper(n)

