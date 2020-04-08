 ##############数组 探索##########

 '''
leetcode.724
寻找中心索引
思路： 1.设置两个滑动窗口，一个装中心索引左边的和，一个装右边的和，初始值分别为 【第零个元素之前的值】，【剩余元素的和】
      2.判断两个窗口的值，若相等，则输出索引值，若不相等，则左边加上当前遍历值，右边减去当前遍历值的下一位值
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        left_sum = sum(nums[:0])
        right_sum = sum(nums[1:])
        for i in range(len(nums) - 1):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            right_sum -= nums[i + 1]
        if left_sum == right_sum:
            return len(nums) - 1
        return -1



'''
leetcode.747
至少时其他数字两倍的最大数
思路： 1.数组排序（sorted）
      2.比较最大数是否是倒数第二大数的至少两倍

'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        sorted_nums=sorted(enumerate(nums),key=lambda x:x[1])
        if sorted_nums[-2][1]==0:
            return sorted_nums[-1][0]
        elif sorted_nums[-1][1]/sorted_nums[-2][1] >= 2:
            return sorted_nums[-1][0]
        else:
            return -1

'''
leetcode.66
加一
思路： 1.列表转字符串
      2.字符串转整数
      3.整数加一
      4.整数转字符串
      5.字符串转列表
'''
 class Solution:
     def plusOne(self, digits: List[int]) -> List[int]:
         s = ''.join([str(x) for x in digits])
         i = int(s)
         i = str(i + 1)

         return [int(x) for x in list(i)]




