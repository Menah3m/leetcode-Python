'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：LeetCode-56
链接：https://leetcode-cn.com/problems/merge-intervals

'''


# 思路： 先排序，然后比较[x1,y1],[x2,y2]中各个值：如果x2大于y1，则不变，否则合并
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res=[intervals[0]]

        for x,y in intervals:
            if res[-1][1] < x:
                res.append([x,y])
            else:
                res[-1][1]=max(y,res[-1][1])
        return res

# 代码2 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        l, r = 0, 1
        intervals = sorted(intervals)
        while r <= len(intervals)-1:
            x1, y1 = intervals[l]
            x2, y2 = intervals[r]
            if x2 > y1:
                l, r = l+1, r+1
            else:
                intervals[l] = (x1, max(y1, y2))
                intervals.pop(r)
        return intervals