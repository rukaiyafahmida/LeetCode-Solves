class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        zz = str(bin(x^y))
        c = 0
        for i in range(len(zz)):
            if zz[i] == '1':
                c+=1
        return c
