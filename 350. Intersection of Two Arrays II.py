class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter1 = dict(Counter(nums1))
        counter2 = dict(Counter(nums2))
        ans = []

        if len(counter1) > len(counter2):
            for key in counter2:
                if key in counter1:
                    ans.extend([key]*min(counter1[key], counter2[key]))
        else:
            for key in counter1:
                if key in counter2:
                    ans.extend([key]*min(counter1[key], counter2[key]))
        return ans
