###########################################
# Let's Have Some Fun
# File Name: counting_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct  5 19:52:58 2018
###########################################

# Counting sort
# 1. linear time, namely O(n)
# 2. out of place
# 3. stable

#coding=utf-8
#!/usr/bin/python

class CountingSort:
    def sort(self, A, k):
        n = len(A)
        C = [0 for _ in range(k)]
        B = [0 for _ in range(n)]
        for i in range(n):
            C[A[i]] += 1
        for i in range(1, k):
            C[i] = C[i] + C[i-1]
        for i in reversed(range(n)):
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
        return B

def showCountingSort(A):
    s = CountingSort()
    print(A)
    B = s.sort(A, 10)
    print(B)


if __name__ == '__main__':
    print('-------case 1---------')
    A = [2, 3, 1, 4]
    showCountingSort(A)
    print('-------case 2---------')
    A = []
    showCountingSort(A)
    print('-------case 3---------')
    A = [1]
    showCountingSort(A)
    print('-------case 4---------')
    A = [1,2,1]
    showCountingSort(A)
