class Solution:
    def totalMoney(self, n: int) -> int:
        a = n//7
        b= n%7
        out = 0
        for i in range(1,a+1):
            out += (i+3)
        out*=7
        extra = (b/2)*(b-1+2*(a+1))
        return out+int(extra)
