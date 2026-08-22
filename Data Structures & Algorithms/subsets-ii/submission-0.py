class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        def backtrack(i,sub):
            
            if i>=len(nums):
                res.append(sub.copy())
                return

            sub.append(nums[i])
            backtrack(i+1,sub) 
            while i<len(nums)-1 and (nums[i+1]==nums[i]):
                i+=1
            sub.pop()
            backtrack(i+1,sub)
        backtrack(0,[])
        return res
