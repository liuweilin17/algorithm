# This minHeap
class Heap:
    def __init__(self, arr):
        self.heap = arr[:]
        self.makeHeap()

    def heapify(self, arr, i):
        while i < len(arr):
            left = 2 * i + 1
            right = 2 * i + 2
            # pop down

    def makeHeap(self):
        n = len(self.heap)
        for i in range(n//2 + 1, 0, -1):
            self.heapify(self.heap, i)