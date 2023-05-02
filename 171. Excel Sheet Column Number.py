class Solution:
    def titleToNumber(self, c: str) -> int:
        n= len(c)
        out=0
        for i in range(0,n):
            x= ord(c[i]) -64
            out+= pow(26,n-i-1)* x
        return out
