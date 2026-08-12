class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest=0
        for j,val in enumerate(nums):
            if furthest<j:
                return False
            elif furthest>=len(nums)-1:
                return True
            furthest=max(furthest,j+val)