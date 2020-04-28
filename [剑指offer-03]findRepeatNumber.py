
'''思路：创建空集合，判断数组元素是否已存在，
  如果存在，则说明重复，返回该值，如果不存在，则添加到集合中
  时间复杂度 O(n)
'''
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)