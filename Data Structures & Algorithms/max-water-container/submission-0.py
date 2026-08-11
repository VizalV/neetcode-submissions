class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min of the 2 bar's height is the length
        # len(sliced arr) is the breadth
        # calculate max area.
        # moving condition should be which adjacent is larger.
        l=0
        r=len(heights)-1
        if heights==[]:
            return 0
        max_water=0
        curr_area=0
        while l<r:
            length=min(heights[l],heights[r])
            breadth=r-l
            curr_area=length * breadth
            max_water=max(max_water,curr_area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1

        return max_water