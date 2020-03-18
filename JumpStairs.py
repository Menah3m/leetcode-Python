# Name:JumpStairs
# Author:Yasu
# Time:2020/3/18

class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return False

        res = [1,1,2]

        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return (res[n]%(1000000007))