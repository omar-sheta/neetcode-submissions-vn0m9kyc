class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        biggest = 0
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            if min(heights[l],heights[r]) == heights[l]:
                l+=1
            else:
                r-=1
            biggest = max(biggest, area)

        return biggest