
# in place and faster
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        make_sum = 0
        curr = head.next
        last_zero = head
        while curr:
            make_sum += curr.val
            if curr.val == 0:
                temp = curr
                curr.val = make_sum
                last_zero.next = curr
                last_zero = temp
                make_sum = 0
            curr = curr.next
        return head.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printNodes(self, heads: ListNode):
        cur = heads
        while cur:
            print(cur.val)
            cur = cur.next

    def makeList(self, arr):
        curr = ListNode()
        temp = curr
        for x in arr:
            temp.next = ListNode(x)
            temp = temp.next
        return curr.next

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        make_sum = 0
        curr = head.next
        while curr:
            make_sum += curr.val
            if curr.val == 0:
                out.append(make_sum)
                make_sum = 0
            curr = curr.next
        return self.makeList(out)
