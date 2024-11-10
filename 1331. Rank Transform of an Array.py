class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        z = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [z[a] for a in arr]
