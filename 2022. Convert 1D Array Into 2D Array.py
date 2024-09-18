class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if len(original) != m*n:
            return out
        d = 0
        for i in range(m):
            out.append(original[d:d + n])
            d += n
        return out
