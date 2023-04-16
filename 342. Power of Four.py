class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = log(n,4)
        if res == int(res):
            return True
        return False
