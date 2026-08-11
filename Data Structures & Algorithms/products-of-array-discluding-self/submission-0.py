class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            answer[i]=nums[i-1]*answer[i-1]
        right_product = [1 for i in range(len(nums))]

        for i in range(len(nums)-2,-1,-1):
            right_product[i]=nums[i+1]*right_product[i+1]
            answer[i]*=right_product[i]
        
        return answer