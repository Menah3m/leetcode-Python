
'''
BubbleSort
时间复杂度:O(n*n)
'''
class Solution(object):
    def bubbleSort(self, nums):
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



'''
SelectSort
时间复杂度：O(n*n)
'''
class Solution(object):
    def selectSort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        le = len(nums)
        for i in range(le):
            for j in range(i, le):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums


'''
QuickSort
时间复杂度：最差O(n*n)  平均O(nlogn)

'''


def partition(nums, l, r):
    pivot = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def quickSort(nums, l, r):
    if l < r:
        pivot_index = partition(nums, l, r)
        quickSort(nums, l, pivot_index - 1)
        quickSort(nums, pivot_index + 1, r)
    return nums

'''
Quicksort 代码2
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)

    def quickSort(self, nums):
        if len(nums) < 2:
            return nums

        before, after = [], []
        pivot = nums.pop()
        for i in range(len(nums)):
            if nums[i] < pivot:
                before.append(nums[i])
            else:
                after.append(nums[i])

        return self.quickSort(before) + [pivot] + self.quickSort(after)

