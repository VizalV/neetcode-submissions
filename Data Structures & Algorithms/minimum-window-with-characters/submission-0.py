class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        if len(t)>len(s):
            return ""
        need={}
        for c in t:
            if c in need:
                need[c]+=1
            else:
                need[c]=1
        L=0
        R=0
        res=[-1,-1]
        need_count=len(need)
        have_count=0
        have={}
        minWindow=float('inf')
        for key,_ in need.items():
            have[key]=0
        while R<len(s):
            if s[R] in need:
                have[s[R]]+=1
                if have[s[R]]==need[s[R]]:
                    have_count+=1
            while have_count==need_count:
                if (R - L + 1) < minWindow:
                    minWindow = R - L + 1
                    res[0] = L
                    res[1] = R
                
                if s[L] in need:
                    have[s[L]]-=1
                    if (have[s[L]]-need[s[L]])<0:
                        have_count-=1
                L+=1
            R+=1
        if minWindow != float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""


        
        
