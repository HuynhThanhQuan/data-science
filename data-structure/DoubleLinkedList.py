# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:59:16 2018

@author: ASUS
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.pre = None
        self.next = None
        
class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def printAll(self):
        p = self.head
        while p is not None:
            print(p.value)
            p = p.next
    def addFirst(self, val):
        node = Node(val)
        if self.isEmpty() == False:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
            
if __name__ == '__main__':
    DLL = DLList()
    DLL.addFirst(1)
    DLL.addFirst(2)
    DLL.addFirst(3)
    DLL.printAll()