class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        x = nums.copy()
        out = [x[i:i + 3] for i in range(0, len(x), 3)]
        for lis in out:
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    if abs(lis[i] - lis[j]) > k:
                        return []

        return out
