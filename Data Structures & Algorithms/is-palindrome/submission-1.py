class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j= len(s)-1
        while(i<j):
            while (s[i].isalnum())==0 and i<j:
                i+=1
            while (s[j].isalnum())==0 and i<j:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1    
        return True