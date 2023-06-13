class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        out= False
        if(n<=0):
            return False
        for x in range(0,66):
            if (pow(3,x) == n):
                out= True
                break
        return out
    
    
    
    
