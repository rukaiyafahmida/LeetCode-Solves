class Solution:
    def largestGoodInteger(self, num: str) -> str:
        coll = set()
        rng = len(num)-2
        try:
            for i in range(rng):
                if num[i] == num[i+1] and num[i+1] == num[i+2]:
                    coll.add(num[i])
        except Exception:
            pass
        if coll:
            return (max(coll))*3
        return ""
