class Solution:
    def is_odd(self, num):
        return num % 2 != 0

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for x, y, z in zip(arr, arr[1:], arr[2:]):
            if self.is_odd(x) and self.is_odd(y) and self.is_odd(z):
                return True
        return False
