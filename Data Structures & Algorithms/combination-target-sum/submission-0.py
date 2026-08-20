class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,subtree,total):
            if total==target:
                res.append(subtree.copy())
                return
            if total>target or i>=len(nums):
                return
            subtree.append(nums[i])
            dfs(i,subtree,total+nums[i])
            subtree.pop()
            dfs(i+1,subtree,total)
        dfs(0,[],0)

        return res