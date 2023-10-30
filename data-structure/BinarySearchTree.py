# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:07:32 2018

@author: ASUS
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def add(self, val):
        n = Node(val)
        if self.isEmpty() == True:
            self.root = n 
        else:
            temp = self.root
            while (temp is not None):
                pre = temp
                if val < temp.val:
                    temp = temp.left
                else:
                    temp = temp.right
            if val < pre.val:
                pre.left = n
            else:
                pre.right = n
    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print(' ', t.val)
            self.inorder(t.right)
    def preorder(self, t):
        if t is not None:
            print(' ', t.val)
            self.preorder(t.left)
            self.preorder(t.right)
    def postorder(self, t):
        if t is not None:
            self.postorder(t.left)
            self.postorder(t.right)
            print(' ', t.val)
    def findLeafs(self, t):
        if t.left == None and t.right == None:
            print(t.val)
        else:
            if t.left != None:
                self.findLeafs(t.left)
            if t.right != None:
                self.findLeafs(t.right)
    def CountLeaf(self, t):
        if t is None:
            return 0
        if t.left is None and t.right is None:
            print(' ', t.val)
            return 1
        return self.CountLeaf(t.left) + self.CountLeaf(t.right)
    def findNodeHasOneChild(self, t):
        if t is not None:
            if t.left == None and t.right != None:
                print(t.val)
                self.findNodeHasOneChild(t.right)
                return 1
            if t.right == None and t.left != None:
                print(t.val)
                self.findNodeHasOneChild(t.left)
                return 1
            if t.right != None and t.left != None:
                return self.findNodeHasOneChild(t.left) + self.findNodeHasOneChild(t.right)
        return 0
    def findNodeHas2SubNode(self, t):
        if t is not None:
            if t.left != None and t.right != None:
                print(t.val)
                self.findNodeHas2SubNode(t.left)
                self.findNodeHas2SubNode(t.right)
                return 1
            return 0
        return 0
    def findHeightOfTree(self, t):
        if t is not None:
            if t.left == None and t.right == None:
                return 1
            return self.findHeightOfTree(t.left) + self.findHeightOfTree(t.right)
        return 0
    def printBFT(self, t, k):
        if (k > 1):
            if t is not None:
                k -= 1
                self.printBFT(t.left, k)
                self.printBFT(t.right, k)
        else:
            if t is not None:
                print(t.val)
    def leftMost(self, t):
        if t.left is not None:
            self.leftMost(t.left)
        else:
            print(t.val)
    def leftMostOfRoot(self):
        temp = self.root.right
        if temp is not None:
            self.leftMost(temp)
        else:
            print(temp)
    def rightMost(self, t):
        if t.right is not None:
            self.rightMost(t.right)
        else:
            print(t.val)
    def rightMostOfRoot(self):
        temp = self.root.left
        if temp is not None:
            self.rightMost(temp)
        else:
            print(temp)
    def getNode(self, t, val):
        if t is not None:
            if t.val == val:
                print('Found', t.val)
                return t
            else:
                self.getNode(t.left, val)
                self.getNode(t.right, val)
    def findRightMostOfNode(self, val):
        node = self.getNode(self.root, val)
        print('Found node' , node)
        if node is not None:
            if node.left is None:
                return node
            else:
                return self.findRightMostOfNode(node.left)
    
    def findLeftMostOfNode(self, t):
        node = self.getNode(self.root)
        print('Found node' , node, node.val)
        if node is not None:
            if node.left is None:
                return node
            else:
                return self.findRightMostOfNode(node.left)
    
if __name__ == '__main__':
    a=[5,4,7,3,6,8]
    t = BST()
    for i in a:
        t.add(i)
    #t.inorder(t.root)
    #t.preorder(t.root)
    #t.postorder(t.root)
    #t.findLeafs(t.root)
    #print('Number of node has 1 node: ', t.findNodeHasOneChild(t.root))
    #print(t.CountLeaf(t.root))
    #print('Number of node has 2 nodes: ', t.findNodeHas2SubNode(t.root))
    #print(t.findHeightOfTree(t.root))
    '''
    for i in range(1, t.findHeightOfTree(t.root) + 1):
        print('Level',i)
        t.printBFT(t.root,i)
    '''
    #t.leftMostOfRoot()
    #t.rightMostOfRoot()
    print(t.findRightMostOfNode(7))