class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(-1)
        n= len(nums)
        
        x=-1
        
        for i in range(0,n):
            if(nums[i] != i):
                x=i
                break
        return x
