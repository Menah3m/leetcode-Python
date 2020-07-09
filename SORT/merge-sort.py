"""
归并排序
1.先分组
2.分别从两个组中按照大小取值（归并）
时间复杂度： O(nlogn)
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    l, r = 0, 0 
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]

    return res

nums = [1,23,7,9,80,64,5]
print(merge_sort(nums))