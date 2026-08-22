class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #()()
        #(())
        res=[]
        def backtrack(perm,open_c,closed_c):
            if open_c==closed_c==n:
                res.append(perm)
                return
            
            if open_c<n:
                backtrack(perm+"(",open_c+1,closed_c)
            if closed_c<open_c:
                backtrack(perm+")",open_c,closed_c+1)
            
        backtrack("",0,0)
        return res