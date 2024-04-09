class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c = 0
        length = len(tickets)
        while tickets[k] > 0:
            inner_c = 0
            for i in range(length):
                if tickets[k] <=0:
                    break
                curr = tickets[i]
                if curr <= 0:
                    continue
                inner_c += 1
                tickets[i] -= 1
            c += inner_c
        return c
