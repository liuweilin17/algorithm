###########################################
# Let's Have Some Fun
# File Name: 20.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 16 21:01:04 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if len(stack) == 0:
                if c in [')', ']', '}']:
                    return False
                else:
                    stack.append(c)
            else:
                if c in ['(', '[', '{']:
                   stack.append(c)
                else:
                    tmp = stack[-1]
                    if (tmp, c) in [('(',')'),('[', ']'),('{', '}')]:
                        stack.pop()
                    else:
                        return False
        if len(stack) != 0:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('(]'))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))

