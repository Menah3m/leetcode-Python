'''
QuickSort
时间复杂度：最差O(n*n)  平均O(nlogn)
要点：
1.确定pivot
2.确定partition的位置
3.递归调用
'''


def partition(nums, start, end):
    pivot = nums[end]
    slow = start - 1
    for fast in range(start, end):
        if nums[fast] < pivot:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
    nums[slow+1], nums[end] = nums[end], nums[slow+1]
    return slow + 1


def quickSort(nums, start, end):
    if start < end:
        pivot_index = partition(nums, start, end)
        quickSort(nums, start, pivot_index - 1)
        quickSort(nums, pivot_index + 1, end)
    return nums

def QuickSort(nums):
    quickSort(nums, 0 , len(nums)-1)
    return nums
'''
Quicksort 代码2
使用额外的数组空间
递归实现
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
