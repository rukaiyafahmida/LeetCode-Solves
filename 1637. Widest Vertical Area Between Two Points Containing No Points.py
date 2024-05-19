class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = [k[0] for k in points]
        p.sort()
        diff = -1
        for one, two in zip(p, p[1:]):
            diff = max(diff, two-one)
        return diff
