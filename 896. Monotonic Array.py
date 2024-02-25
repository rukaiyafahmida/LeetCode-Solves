class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up = False
        down = False
        len_N = len(nums)
        if len_N == 1:
            return True
        for i in range(len_N):
            try:
                if nums[i] > nums[i + 1]:
                    down = True
                elif nums[i] < nums[i + 1]:
                    up = True
                if up and down:
                    return False
            except:
                pass
        return True
