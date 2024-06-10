class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        if expected == heights:
            return 0
        out = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                out += 1
        return out
