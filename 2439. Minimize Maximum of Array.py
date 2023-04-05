class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:        
        total_sum = 0
        result = 0
        for index, num in enumerate(nums):
            total_sum += num
            
            result = max(result, (total_sum + index) // (index + 1))
        return int(result)
