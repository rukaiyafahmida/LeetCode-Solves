# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToNumber(self, head: ListNode):
        curr = head
        num = 0
        i = 0
        while curr:
            num += curr.val * (10 ** i)
            i += 1
            curr = curr.next
        return num

    def numberToList(self, num: int):
        head = ListNode()
        if num == 0:
            return head
        curr = head
        while num != 0:
            temp = ListNode(num % 10)
            curr.next = temp
            curr = curr.next
            num = num//10
        return head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.listToNumber(l1)
        num2 = self.listToNumber(l2)
        res = num1 + num2
        list_res = self.numberToList(res)
        return list_res
