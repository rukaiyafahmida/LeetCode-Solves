class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        s_m, s_p, s_g = 0, 0, 0

        for i, bins in enumerate(garbage):
            if "M" in bins:
                s_m = i
            if "P" in bins:
                s_p = i
            if "G" in bins:
                s_g = i

        total = len("".join(garbage)) + sum(travel[:s_p]) + sum(travel[:s_g]) + sum(travel[:s_m])

        return total
