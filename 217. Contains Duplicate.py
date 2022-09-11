class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        out=False
        
        if(len(nums)> len(set(nums))):
            out=True
        return out
            
