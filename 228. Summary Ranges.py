class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l = len(nums)
        output = []
        cont = True
        start = nums[0]
        for i in range(l):
            if i == l - 1:
                if start == nums[i]:
                    output.append(f"{nums[i]}")
                elif cont:
                    output.append(f"{start}->{nums[i]}")
                continue

            if nums[i] + 1 != nums[i + 1]:  # no seq so break
                if start == nums[i]:
                    output.append(f"{nums[i]}")
                else:
                    output.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
                cont = False
                continue
            else:
                cont = True

        return output
