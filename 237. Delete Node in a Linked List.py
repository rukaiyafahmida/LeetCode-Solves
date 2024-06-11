# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur.next:
            cur.val = cur.next.val
            prev = cur
            cur = cur.next
            if not cur.next:
                prev.next = None
                break
