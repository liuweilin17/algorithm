###########################################
# Let's Have Some Fun
# File Name: 93.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 17 Aug 01:29:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#93. Restore IP Addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # invalid IP: [0, 255] * 4
        ret = []
        def helper(tmp, start):
            if len(tmp) == 4:
                if start == len(s):
                    ret.append('.'.join(tmp))
                return

            # Notice len(s)+1 instead of len(s)
            for end in range(start+1, min(start+4, len(s)+1)):
                if 0 <= int(s[start:end]) <= 255:
                    if end-start > 1 and s[start] == '0': # str started with 0 is invalid
                        break
                    helper(tmp + [s[start:end]], end)

        helper([], 0)
        return ret



