class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        c = 0
        for num in nums:
            c+=num
            output.append(c)
        return output
            
