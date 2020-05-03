class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or max(height) == 0: return 0
        self.res = 0
        max_ = max(height)
        index = height.index(max_)
        self.subtrap(height[:index])
        self.subtrap(height[index+1:][::-1])
        return self.res

    def subtrap(self, h):
        if len(h) == 0 or max(h) == 0: return 0
        maxh = max(h)
        index = h.index(maxh)
        self.res += (len(h)-index-1)*maxh - sum(h[index+1:])
        self.subtrap(h[:index])