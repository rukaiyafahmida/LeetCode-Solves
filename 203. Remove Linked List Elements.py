class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = ListNode()
        while curr:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                prev.next = curr.next
                curr = prev.next
                continue
            prev = curr
            curr = curr.next
        return head
