class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=1
        curr_len=1
        i=0
        j=1
        d=set()
        if s:
            d.add(s[i])
        else:
            return 0
        while j<len(s):
            if s[j] not in d:
                d.add(s[j])
                curr_len+=1
                max_len=max(max_len,curr_len)
                j+=1
            else:
                while s[i]!=s[j]:
                    d.remove(s[i])
                    i+=1
                d.add(s[j])
                i+=1
                j+=1
                curr_len=j-i
                max_len=max(max_len,curr_len)
        return max_len
