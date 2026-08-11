class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,val in enumerate(nums):
            d[val] = i
        for i,val in enumerate(nums):
            if (target - val) in d and d[target-val]!=i:
                return [i,d[target-val]]