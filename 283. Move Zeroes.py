class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index=[]
        length=len(nums)
        
        for i in range(0,length):
            if(nums[i]==0):
                index.append(i)
        x=0
        for i in index:
            del nums[i-x]
            x+=1
            nums.append(0)
            
