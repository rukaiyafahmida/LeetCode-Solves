class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n>1:
            if n%2 ==0:
                n=n//2
                matches+=n
            else:
                matches+=(n-1)//2
                n=(n+1)//2
        return int(matches)
