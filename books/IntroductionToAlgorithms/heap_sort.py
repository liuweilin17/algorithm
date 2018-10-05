###########################################
# Let's Have Some Fun
# File Name: heap_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct  5 15:36:14 2018
# HeapSort in Introduction to Algorithms
# Heap is a nearly complete binary tree, namely complete except the leaves layer
# mapHeapify: O(logn)
# buildMaxHeap: O(n)
# heapSort:
# 1. worst case O(nlogn)
# 2. in-place sort
# 3. unstable. For example, a max heap, last two leaves are 0,0. After the swap and heapifiy,
# the last 0 probably in the front of the second 0
###########################################
#coding=utf-8
#!/usr/bin/python 
# max heap
class HeapSort:
    def getLeft(self, i):
        return 2*i + 1

    def getRight(self, i):
        return 2*i + 2

    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    def maxHeapify(self, A, i, end):
        l = self.getLeft(i)
        r = self.getRight(i)
        if l < end and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < end and A[r] > A[largest]:
            largest = r
        if largest != i:
            self.swap(A, i, largest)
            self.maxHeapify(A, largest, end)

    # without recursion and swap
    def maxHeapifyNew(self, A, i, end):
        if i >= end:
            return
        org = A[i]
        while(True):
            l = self.getLeft(i)
            r = self.getRight(i)
            if l < end and A[l] > A[i]:
                largest = l
            else:
                largest = i
            if r < end and A[r] > A[largest]:
                largest = r
            if largest != i:
                A[i] = A[largest]
                i = largest
            else:
                break
        A[i] = org

    def buildMaxHeap(self, A):
        # the first i is: the last node with leaves in the tree
        # namely, the max i, which 2i + 1 < n
        # i < (n-1)/2
        # if n is odd,  i < (n - 1) / 2 = n / 2
        # if n is even, i < (n - 1) / 2 = n / 2 - 1
        # so, when i<n/2, satisfies two ifs.
        n = len(A)
        i = n/2
        while (i>=0):
            self.maxHeapifyNew(A, i, n)
            #self.maxHeapify(A, i, n)
            i -= 1

    def heapSort(self, A):
        i = len(A) - 1
        while(i >= 1):
            self.swap(A, i, 0)
            self.maxHeapifyNew(A, 0, i)
            i -= 1

def showHeapSort(A):
    s = HeapSort()
    print A
    s.buildMaxHeap(A)
    print A
    s.heapSort(A)
    print A

if __name__ == '__main__':
    s = HeapSort()
    print '-------case 1---------'
    A = [2, 3, 1, 4]
    showHeapSort(A)
    print '-------case 2---------'
    A = []
    showHeapSort(A)
    print '-------case 3---------'
    A = [1]
    showHeapSort(A)
    print '-------case 4---------'
    A = [1,2,1]
    showHeapSort(A)
