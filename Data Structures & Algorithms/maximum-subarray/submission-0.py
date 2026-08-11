class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum=0
        max_sum=float('-inf')
        for i,val in enumerate(nums):
            running_sum+=val
            max_sum=max(running_sum,max_sum)
            if running_sum<0:
                running_sum=0
        return max_sum