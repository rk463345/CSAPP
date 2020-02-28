#!/usr/bin/env python3

"""
Script used to solve Phase_6 in CSAPP Binary Bomb Lab
"""

from itertools import permutations

class node:
    def __init__(self, address, value, number):
        self.address = address
        self.value = value
        self.number = number
        self.next_node = None

    def set_next(self, next_node):
        self.next_node = next_node

def phase_6(ints):
    #creates the necessary nodes
    # change the values to match the values from your linked list
    node1 = node(0x006042f0, 0x213, 0x1)
    node2 = node(0x00604300, 0xe9,  0x2)
    node3 = node(0x00604310, 0x16e, 0x3)
    node4 = node(0x00604320, 0x331, 0x4)
    node5 = node(0x00604330, 0x143, 0x5)
    node6 = node(0x00304340, 0x352, 0x6)
    nodeN = node(0x00000000, 0x0,   0x0)
    node1.set_next(node2)
    node2.set_next(node3)
    node3.set_next(node4)
    node4.set_next(node5)
    node5.set_next(node6)
    node6.set_next(nodeN)
    a = []   
    """# checks that the numbers are unique
    if len(ints) != len(set(ints)):
        return False
    # checks that numbers are less than 6 
    if max(ints)-1 > 5:
        return False"""
    # creates the node array
    for i in range(6):
        n = node1
        for j in range(1, ints[i]):
            n = n.next_node
        a.append( n )
    # creates the connections for the nodes
    for i in range(1,6):
        a[i-1].set_next( a[i] )
    a[5].set_next(nodeN)
    n = a[0]
    for i in range(6):
        if n.value < n.next_node.value:
            return False
        n = n.next_node 
    return True

def permutation():
    for x in permutations('123456', 6):
        ints = []
        for i in range(len(x)):
            ints.append( int(x[i]))

        if (phase_6(ints)):
            for j in range(0,6):
                ints[j] = abs(ints[j] - 7)
            print('Answer: ', ints)

if __name__ == "__main__":
    permutation()
