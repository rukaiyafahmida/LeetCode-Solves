from functools import lru_cache

class Solution:
    lists = [1, 2]
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
