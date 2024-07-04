class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        l = 0
        r = n
        while l <= r:
            m = (l + r) // 2
            resp = guess(m)
            if resp == -1:
                r = m-1
            elif resp == 1:
                l = m+1
            else:
                return m
