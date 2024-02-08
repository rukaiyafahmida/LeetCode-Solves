class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out = 0
        temp = 0
        flag = False
        for num in nums:
            if num == 1:
                if flag:
                    temp += 1
                else:
                    temp = 1
                    flag = True
            else:
                out = max(out, temp)
                temp = 0
                flag = False

        out = max(out, temp)
        return out
