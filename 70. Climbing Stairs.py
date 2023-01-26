class Solution:
    def climbStairs(self, n):
        a,b = 1,0
        for i in range(n):
            a,b = a+b,a
        return a
