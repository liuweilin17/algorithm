class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, x): # x is an array of elements
        l = len(x)
        if l < 1:
            return None
        else:
            self.head = ListNode(x[0])
            self.tail = self.head
            for i in range(1, l):
                nd = ListNode(x[i])
                self.tail.next = nd
                self.tail = nd

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

def printList(head):
    p = head
    while(p):
        print(p.val, end=' ')
        p = p.next