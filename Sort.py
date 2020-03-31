
'''
QuickSort
时间复杂度:O(n*n)


'''

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        le = len(nums)
        for i in range(le-1):
            for j in range(le-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums