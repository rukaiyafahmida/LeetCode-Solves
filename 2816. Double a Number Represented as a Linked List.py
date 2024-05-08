class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        int_list = []
        while curr:
            int_list.append(curr.val)
            curr = curr.next
        in_hand = list()
        len_int = len(int_list)
        curr = None
        prev = None
        for i, n in enumerate(int_list[::-1]):
            try:
                in_hand_val = in_hand.pop()
            except:
                in_hand_val = 0
            mul = n*2 + in_hand_val
            curr = ListNode(mul % 10)
            curr.next = prev
            prev = curr
            pp = mul//10
            if pp != 0:
                in_hand.append(pp)
            if i+1 == len_int and in_hand:
                new_node = ListNode(in_hand.pop())
                new_node.next = curr
                return new_node
        return curr
