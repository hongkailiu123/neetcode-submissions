class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        water = 0
        for i in range(length):
            currHeight = height[i]
            maxLeft = max(height[0:i+1])
            maxRight = max(height[i: length])
            water += min(maxLeft, maxRight) - currHeight
        
        return water









    