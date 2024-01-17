class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        out = c.items()
        ax = [a[1] for a in out]
        return len(ax) == len(set(ax))
