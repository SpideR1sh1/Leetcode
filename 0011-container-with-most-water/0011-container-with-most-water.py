class Solution:
    def maxArea(self, height: List[int]) -> int:
        resArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            width = r - l
            resArea = max(resArea, min(height[l], height[r]) * width)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return resArea

