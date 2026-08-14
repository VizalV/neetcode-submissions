class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i,val in enumerate(nums):
            if val in d:
                d[val]+=1
            else:
                d[val]=1
        for k,v in d.items():
            if v==1:
                return k