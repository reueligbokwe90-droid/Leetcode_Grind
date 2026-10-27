class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        #empty array
        if not heights:
            return 0
        
        for x in range(len(heights)):
            for z in range(x+1,len(heights)):
                maxHeight = min(heights[x],heights[z])
                width = abs(z - x)
                area = max(area, maxHeight * width)
        return area