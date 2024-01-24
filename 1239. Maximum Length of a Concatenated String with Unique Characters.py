class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l = len(arr)
        sample = [list(itertools.combinations(arr, i)) for i in range(0, l + 1)]
        maxim = -1
        for lis in sample:
            for tup in lis:
                curr = "".join(tup)
                len_curr = len(curr)
                if maxim < len_curr:
                    if len_curr == len(set(curr)):
                        maxim = len_curr
        return maxim
