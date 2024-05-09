class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        summed = sum(prices[:2])
        if summed <= money:
            return money-summed
        return money
