# -*- coding: utf-8 -*-
"""
Created on Sun May 20 13:28:40 2018

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


class StackByLinkedList:
    def __init__(self):
        self.llist = SLList()
    def push(self, value):
        self.llist.addLast(value)
    def pop(self):
        result = self.llist.get(self.llist.size() - 1)
        self.llist.removeLast()
        return result
    def isEmpty(self):
        return self.llist.isEmpty()
    def peek(self):
        return self.llist.get(self.llist.size()-1)
    def size(self):
        return self.llist.size()
    
if __name__ == '__main__':
    #test = StackByLinkedList()
    #test.push(1)
    #test.push(2)
    #test.push(4)
    #print(test.pop())
    #print(test.pop())
    #print(test.pop())
    #print(test.peek())
    #print(test.size())
    #print(test.isEmpty())
    x = int(input('Enter your Heximal Number: '))
    s = StackByLinkedList()
    d = x//2
    while d>0:
        s.push(x % 2)
        x = d
        d = x//2
       
    s.push(x%2)
    print('Stack')
    while s.isEmpty() == False:
        print(s.pop())