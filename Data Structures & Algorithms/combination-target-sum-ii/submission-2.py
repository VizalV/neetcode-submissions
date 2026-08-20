class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(idx,sub,total):
            if total==target:
                res.append(sub.copy())
                return
            if idx==len(candidates) or total>target:
                return

            sub.append(candidates[idx])
            dfs(idx+1,sub,total+candidates[idx])
            sub.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1,sub,total)
        
        dfs(0,[],0)
        return res