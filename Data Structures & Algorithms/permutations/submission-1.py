class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in nums:
                if i in perm:
                    continue
                else:
                    perm.append(i)
                    dfs(perm)
                    perm.pop()
        dfs([])
        return res