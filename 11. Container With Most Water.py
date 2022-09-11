class Solution:
    def maxArea(self, h: List[int]) -> int: 
        m=-1
        j=len(h)-1
        i=0
        
        while i < j:
            m = max( m, ((j-i)* min(h[i],h[j])))
            if(h[i]<h[j]):
                i+=1
            else:
                j-=1
           
        #print(m)
        return m
