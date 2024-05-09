class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for n in nums:
            if n < 0:
                break
            if (n * -1) in nums:
                return n
        return -1
