class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i_1, i_2 = 0, 0
        while i_1 < m and i_2 < n:
            while i_1 < m and i_2 < n and nums1[i_1] <= nums2[i_2]:
                res.append(nums1[i_1])
                i_1 += 1
            while i_1 < m and i_2 < n and nums1[i_1] > nums2[i_2]:
                res.append(nums2[i_2])
                i_2 += 1
        
        while i_1 < m:
            res.append(nums1[i_1])
            i_1 += 1

        while i_2 < n:
            res.append(nums2[i_2])
            i_2 += 1    
    
        for i in range(len(nums1)):
            nums1[i] = res[i]