class Solution:
    def partitionString(self, s: str) -> int:
        un = ''
        count = 0
        for c in s:
            if c in un:
                un = c
                count+=1
            else:
                un +=c
        return count+1
