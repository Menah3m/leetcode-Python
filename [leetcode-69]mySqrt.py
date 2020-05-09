'''
二分法求平方根：
1.设置左右边界，左边界为0，右边界为x
2.当左边界不大于右边界时，执行判断
3.判断方式：取中值mid，判断mid的平方与x的大小关系：
           如果mid的平方不大于x，则将mid作为暂定的近似值，同时将左边界更新为mid+1（因为所求结果为整数）
           如果mid的平方大于x，则将由边界更新为mid-1
4.判断循环结束后，返回res
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, res = 0, x, -1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid -1
        return res 