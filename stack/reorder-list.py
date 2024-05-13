# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # split the list in half using slow & fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = prev  = None

        # reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge them together 
        first = head
        second = prev
        while second:
            tmp1 = first.next 
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2