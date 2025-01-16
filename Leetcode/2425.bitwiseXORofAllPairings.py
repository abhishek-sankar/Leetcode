class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) %2 == 0 and len(nums2) %2 == 0:
            return 0
        elif len(nums1) %2 == 0:
            res = reduce(lambda x, y: x ^ y, nums1)
        elif len(nums2) %2 == 0:
            res = reduce(lambda x, y: x ^ y, nums2)
        else:
            res = reduce(lambda x, y: x ^ y, nums2 + nums1)

        return res