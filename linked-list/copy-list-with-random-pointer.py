"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        # clone the nodes
        hashMap = { None : None }
        curr = head
        while curr:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next

        # set the pointers: next and random pointers
        curr = head
        while curr:
            copy = hashMap[curr]
            copy.next = hashMap[curr.next]
            copy.random = hashMap[curr.random]
            curr = curr.next
        return hashMap[head]