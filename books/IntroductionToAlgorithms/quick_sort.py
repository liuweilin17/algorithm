# coding=utf-8
###########################################
# Let's Have Some Fun
# File Name: quick_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct  5 19:52:38 2018
###########################################
#!/usr/bin/python

# QuickSort
# 1.worst case: T(n) = T(n-1) + T(0) + Θ(n) => T(n)=O(n²)
# 2.Best case: T(n) = 2T(n/2) + Θ(n) => T(n) = O(nlogn)
# 3.Balanced case: T(n) = T(n*(1/a)) + T(n*(1-1/a)) => T(n)=O(nlogn), for all a>=1
# 4.in place sort
# 5.unstable


import random

class QuickSort:
    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    def partition1(self, A, p, r):
        i = p-1
        pivot = A[r]
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                self.swap(A, i, j)
        self.swap(A, i+1, r)
        return i+1

    # HOARE-PARTITION, the original version
    def partition2(self, A, p, r):
        pivot = A[p]
        i = p - 1
        j = r + 1
        while(True):
            condition = True
            while condition:
                j -= 1
                if A[j] <= pivot:
                    break
            while condition:
                i += 1
                if A[i] >= pivot:
                    break
            if i < j:
                self.swap(A, i, j)
            else:
                return j

    def randomizedPartition(self, A, p, r):
        i = random.randint(p, r)
        self.swap(A, i, r)
        return self.partition1(A, p, r)

    def quick_sort(self, A, p, r):
        if p < r:
            #q = self.partition1(A, p, r)
            #q = self.partition2(A, p, r)
            q = self.randomizedPartition(A, p, r)
            self.quick_sort(A, p, q-1)
            self.quick_sort(A, q+1, r)

    def sort(self, A):
        self.quick_sort(A, 0, len(A)-1)

    def findIth(self, A, p, r, i):
        if p == r:
            return A[p]
        q = self.partition1(A, p, r)
        k = q - p + 1
        if i > r - p + 1:
            return
        if k == i:
            return A[q]
        elif k > i:
            return self.findIth(A, p, q-1, i)
        else:
            return self.findIth(A, q+1, r, i-k)

def showQuickSort(A):
    s = QuickSort()
    print(A)
    s.sort(A)
    print(A)

if __name__ == '__main__':
    print('-------case 1---------')
    A = [2, 3, 1, 4]
    showQuickSort(A)
    print('-------case 2---------')
    A = []
    showQuickSort(A)
    print('-------case 3---------')
    A = [1]
    showQuickSort(A)
    print('-------case 4---------')
    A = [1,2,1]
    showQuickSort(A)

    print('-------find kth ------')
    s = QuickSort()
    A = [4, 1, 5, 2, 3, 3]
    print(s.findIth(A, 0, len(A)-1, 100))
    print(s.findIth(A, 0, len(A)-1, 1))
    print(s.findIth(A, 0, len(A)-1, 3))

