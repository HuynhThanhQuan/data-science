# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:32:10 2018

@author: ASUS
"""

class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def add(self, val):
        node = Node(val)
        if self.isEmpty() == True:
            self.head=self.tail=node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
    def size(self):
        if self.isEmpty() == True:
            return 0
        else:
            count = 1
            cur_node = self.head
            while cur_node != self.tail:
                count+=1
                cur_node = cur_node.next
            return count
    def removeLast(self):
        if self.isEmpty() == False:
            if self.size() == 1:
                self.head = self.tail = None
            else:
                cur_node = self.head
                while cur_node.next != self.tail:
                    cur_node = cur_node.next
                self.tail = cur_node
                self.tail.next = self.head
        
if __name__=='__main__':
    test = CircularQueue()
    print(test.isEmpty())
    print(test.size())
    test.add(3)
    print(test.isEmpty())
    print(test.size())
    test.add(5)
    print(test.size())
    test.add(6)
    test.add(7)
    print(test.size())
    test.removeLast()
    print(test.size())