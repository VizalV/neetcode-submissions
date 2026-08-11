class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0 for i in range(len(height))]
        right_max=[0 for i in range(len(height))]
        water=0
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i+1])
        for i in range(1,len(height)-1):
            water_level=min(left_max[i],right_max[i])-height[i]
            if water_level>0:
                water+=water_level
        return water