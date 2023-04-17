class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        out = [True if x+extraCandies>= maximum else False for x in candies]
        return out
    
