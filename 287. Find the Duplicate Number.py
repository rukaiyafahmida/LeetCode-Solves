class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        x=-1
        for i in range(0,len(nums)):
            if(nums[i] == nums[i+1]):
                x=nums[i]
                break;
        return x
