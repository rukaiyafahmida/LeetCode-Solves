class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0]-arr[1]
        for a,b in zip(arr, arr[1:]):
            if a-b ==diff:
                continue
            else:
                return False
        return True
