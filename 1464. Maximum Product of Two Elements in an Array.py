class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i = nums[-1]
        j = nums[-2]
        return (i-1)*(j-1)
