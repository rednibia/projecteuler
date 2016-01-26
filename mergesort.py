__author__ = 'admin'
import timeit
import math

from random import randint

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor
        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """
        Delete node containing data
        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """
        Compare 2 trees
        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else: # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """
        Return the number of children
        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


class createObject():
    def __init__(self):
        self.value = randint(0, 500000)
        self.word = str(self.value)

def createList(n):
    list = []
    for x in range(0, n):
        list.append(randint(0, 500))
    return list

    list = []
    for x in range(0, n):
        list.append(createObject())
    return list

def printList(list):
    printable = []
    for values in list:
        printable.append(values.word)
    print printable

def quickSort(list):
    if len(list)>1:
        p = list[int(len(list)/2)].value
        low = []
        same = []
        high = []
        for num in list:
            if num.value < p:
                low.append(num)
            elif num.value == p:
                same.append(num)
            else:
                high.append(num)
        return quickSort(low) + same + quickSort(high)
    return list

def binarySearch(list, target):
    cursor = len(list)/2
    if list[cursor].value == target:
        return list[cursor].word
    elif list[cursor].value > target:
        return binarySearch(list[:cursor], target)
    else:
        return binarySearch(list[cursor/2 + 1:], target)


def depth(n):
    return int(math.log( n + 1 ) / math.log( 2 ))

class heap:
    def __init__(self, value):
        self.value = value
        self.child1 = None
        self.child2 = None
    def add(self, new):
        if self.child1 == None:
            self.child1 = heap(new)
        else:
            self.child2 = heap(new)
    def checkHeap(self):
        if self.child1 == None and self.child2 == None:
            return False
        else:
            return True
    def heapAddList(self, newList):
        for x in range(0, len(newList)):
            depth = depth(x)


