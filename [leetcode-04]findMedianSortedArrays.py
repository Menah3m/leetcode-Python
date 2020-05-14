
'''
leetcode-04
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

'''

'''
法1：
#不满足时间复杂度
1.合并两个数组并排序
2.取中位数

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1+nums2
        
        nums.sort()
        ind = (len(nums)-1)//2

        if len(nums) % 2 == 1:
            return float(nums[ind])
        else:
            return (nums[ind]+nums[ind+1])/2
             
