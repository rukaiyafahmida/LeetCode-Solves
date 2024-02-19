class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        c = 0
        cookies = len(s) - 1
        child = len(g) - 1
        while cookies >= 0 and child >= 0:
            if s[cookies] >= g[child]:
                c += 1
                cookies -= 1
                child -= 1
            else:
                child -= 1
        return c
