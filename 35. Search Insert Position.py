class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        n= len(nums)
        j = n-1
      
        while(i<=j):
            m = math.floor((i+j)/2)
            if(nums[m]== target):
                return m
            if(nums[m] > target):
                j=m-1
            if(nums[m] < target):
                i=m+1
        return i
