class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = set(nums1)
        two = set(nums2)
        if len(one) > len(two):
            return [item for item in two if item in one]
        return [item for item in one if item in two]
