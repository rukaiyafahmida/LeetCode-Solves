class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maps = []
        for i, row in enumerate(mat):
            sum = 0
            for val in row:
                sum+=val
            maps.append((sum, i))
        maps.sort()
        out = [val[1] for val in maps[:k]]
        return out
