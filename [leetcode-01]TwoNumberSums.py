# Name:TwoNumberSums
# Author:Yasu
# Time:2020/3/18



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        暴力方法
        '''
        for i in range(len(nums)-1):
            x = target - nums[i]
            nums_new = nums[:]
            nums_new.remove(nums[i])
            if x in nums_new:
                return [i,nums_new.index(x)+1]

'''
思路2：
1. 先排序：将原数组转换成索引序列enu（通过enumerate函数得到),然后通过sorted函数进行排序（选索引序列的值作为排序key ）
2. 定义前后两个指针，将对应的值相加得到sum ，比较sum和target的差距，
   若sum>target, 则后指针减1，
   若sum<target，则前指针加1，
   sum=target 时，输出对应的enu索引序列的下标
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_sorted = sorted(list(enumerate(nums)), key=lambda x: x[1])

        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1, 0, -1):
                while i < j:
                    if nums_sorted[i][1] + nums_sorted[j][1] < target:
                        i += 1
                    elif nums_sorted[i][1] + nums_sorted[j][1] > target:
                        j -= 1
                    else:
                        return [nums_sorted[i][0], nums_sorted[j][0]]


'''
思路三：哈希表
1.创建一个词典
2.key是列表中的数，value是这个数的索引
3.遍历整个list，判断 target-当前位置的数 是否在词典中
  若在，返回value  若不在，添加该位置的数到词典中

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i
        return []