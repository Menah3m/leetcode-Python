'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：LeetCode-11
链接：https://leetcode-cn.com/problems/container-with-most-water

'''



#实质是一个求最大矩形面积问题，面积大小由短的那个垂直线段决定，使用双指针遍历，求出最大面积
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        while True:
            if l > r:
                break
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        temp_area = 0
        l, r = 0, len(height)-1
        while l < r:
            temp_area = (r-l)*min(height[l],height[r])
            max_area = max(temp_area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
            
