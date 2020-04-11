class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1 is None or nums2 is None:
            return nums1
        nums1[m:m+n]=nums2
        nums1.sort()