"""
插入排序：
从第二个数开始遍历，每次都和前面的拍好序的序列进行比较，如果大于则往前置换。
时间复杂度： 最优 O(n)  最坏 O(n^2)

"""


def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

nums = [1,14,75,0,3,709]
print(insert_sort(nums))