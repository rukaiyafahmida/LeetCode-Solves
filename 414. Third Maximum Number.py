class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = [*set(nums)]
        temp.sort()
        return temp[-3] if len(temp)>2 else temp[-1]
