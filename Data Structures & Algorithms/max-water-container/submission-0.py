class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxsf = 0
        for i in range(length):
            leftBar = heights[i]
            for j in range(i + 1, length):
                curr = (j - i) * min(heights[i], heights[j])
                maxsf = max(maxsf, curr)  
        
        return maxsf
        