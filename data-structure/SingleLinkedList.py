# -*- coding: utf-8 -*-
"""
Created on Sun May 20 08:45:57 2018

@author: ASUS
"""

class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def addFirst(self, value):
        p = SLLNode(value)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            p.next = self.head
            self.head = p
    def printAll(self):
        p = self.head
        while p is not None:
            print(p.value)
            p = p.next
    def addLast(self, value):
        p = SLLNode(value)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    def size(self):
        if self.isEmpty():
            return 0
        else:
            p = self.head
            num = 0
            while p is not None:
                num += 1
                p = p.next
            return num
    def get(self, pos):
        if pos >= self.size():
            return None
        else:
            p = self.head
            idx = 0
            while p is not None:
                if idx == pos:
                    return p.value
                p = p.next
                idx += 1
    def addPos(self, pos, value):
        if pos == 0:
            self.addFirst(value)
        elif pos == self.size():
            self.addLast(value)
        elif pos > self.size():
            print('Out of range')
        elif pos < self.size():
            p = SLLNode(value)
            p_iter = self.head
            idx = 0
            while idx < pos - 1:
                p_iter = p_iter.next
                idx += 1
            p.next = p_iter.next
            p_iter.next = p

    def indexOf(self, value):
        if self.isEmpty() == False:
            p = self.head
            idx = 0
            while p is not None:
                if p.value == value:
                    return idx
                p = p.next
                idx +=1
    def removeFirst(self):
        if self.isEmpty() == False:
            if self.size() == 1:
                self.head = None
            else:
                self.head = self.head.next
    def removeLast(self):
        if self.isEmpty() == False:
            if self.size() ==1:
                self.head = self.tail = None
            else:
                p = self.head
                while p.next is not self.tail:
                    p = p.next
                self.tail = p
                self.tail.next = None
    
         
if __name__ == "__main__":
    SLL = SLList()
    SLL.addFirst(20)
    SLL.addFirst(13)
    SLL.addFirst(24)
    SLL.removeFirst()
    SLL.removeFirst()
    SLL.removeFirst()
    SLL.removeFirst()
    SLL.addLast(30)
    SLL.addLast(31)
    SLL.addPos(1, 50)
    
    
    print('Value of position {0} is {1}'.format(1, SLL.get(1))) 
    print('Size of linkedlist is', SLL.size())
    print('Position of {0} is {1}'.format(13, SLL.indexOf(13)))
    print('Position of {0} is {1}'.format(30, SLL.indexOf(30)))
    SLL.printAll()