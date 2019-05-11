###########################################
# Let's Have Some Fun
# File Name: 8.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 12:14:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        if not s: return 0
        print(s)
        pos = True
        if s[0] == '+':
            pos = True
            s = s[1:]
        elif s[0] == '-':
            pos = False
            s = s[1:]
        elif not s[0].isdigit():
            return 0
        else: pass

        ret = 0
        for c in s:
            if c.isdigit():
                ret = ret * 10 + int(c)
                if pos and ret > 2 ** 31 - 1:
                    ret = 2 ** 31 - 1
                    break
                elif not pos and ret > 2 ** 31:
                    ret = 2 ** 31
                    break
            else:
                break

        return ret if pos else -ret

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('  -42'))