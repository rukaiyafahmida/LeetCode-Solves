from typing import List
from itertools import combinations


class Solution:
    def do_xor(self, it):
        xor = 0
        for a in it:
            xor = xor ^ a
        return xor

    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        ans = sum(nums)
        for i in range(2, l + 1):
            x = combinations(nums, i)
            for it in x:
                ans += self.do_xor(it)
        return ans
