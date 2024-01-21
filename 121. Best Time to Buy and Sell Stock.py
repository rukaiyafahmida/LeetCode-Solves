class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lis = []
        n = len(prices)
        for i in range(n):
            ele = -1
            for j in range(i + 1, n):
                dif = prices[j] - prices[i]
                ele = max(ele, dif)
            lis.append(ele)

        diff = max(lis)
        if diff < 0:
            return 0
        return diff
