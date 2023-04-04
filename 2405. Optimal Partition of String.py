class Solution:
    def partitionString(self, s: str) -> int:
        un = []
        count = 0
        for c in s:
            un.append(c)
            if len(un) > len(set(un)):
                un = [c]
                count+=1
        return count+1
