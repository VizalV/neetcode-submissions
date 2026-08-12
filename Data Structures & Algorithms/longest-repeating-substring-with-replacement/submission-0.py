class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #[xxxyyxyyyyxx], k=4
        l=r=0
        d={}
        result=0
        while r<len(s) and l<=r:
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            while (r-l+1)-max(d.values())>k:
                d[s[l]]-=1
                l+=1
            result=max(result,r-l+1)
            r+=1
                
        return result