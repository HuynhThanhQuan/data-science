# -*- coding: utf-8 -*-
"""
Created on Sun May 20 14:38:58 2018

@author: ASUS
"""
class PriorityQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, name, pri):
        if self.size() >= 2:
            if self.items[len(self.items)-1][1] > pri:
                self.items.append((name,pri))
            elif self.items[0][1] < pri:
                self.items.insert(0,(name,pri))
            else:
                for i in range(len(self.items) - 1):
                    if self.items[i][1]>pri and self.items[i+1][1]<pri:
                        self.items.insert(i+1,(name,pri))
                        break
        elif self.size() == 1:
            if pri <= self.items[0][1]:
                self.items.append((name, pri))
            else:
                self.items.insert(0, (name, pri))
        elif self.size() == 0:
            self.items.append((name, pri))
            '''
    def enqueue(self, name, pri):
        if self.isEmpty() == True:
            self.items.append((name, pri))
        else:
            i = 0
            if self.items[len(self.items)-1][1]>pri:
                self.items.insert(len(self.items), (name, pri))
            else:
                while (pri>self.items[i][1]):
                    i += 1
                self.items.insert(i, (name, pri))
                '''
    def dequeue(self):
        if self.isEmpty():
            print('Nothing to dequeue')
        else:
            a, b = self.items[0]
            self.items.remove(self.items[0])
            return a, b
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    def front(self):
        return self.items[0]
