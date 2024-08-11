class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        count = 0
        for item in c.items():
            if item[1] == 1:
                count += 1
                if k == count:
                    return item[0]
        return ""
