class Solution:
    def largestGoodInteger(self, num: str) -> str:
        coll = set()
        for i in range(len(num)-3):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                coll.add(num[i])
        if coll:
            return (max(coll))*3
        return ""
