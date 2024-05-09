class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        out = 0
        for i in range(k):
            val = happiness.pop() - i
            if val <= 0:
                break
            out += val
        return out
