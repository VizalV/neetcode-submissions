class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in d.keys():
                d[sorted_word]=[]
                d[sorted_word].append(word)
            else:
                d[sorted_word].append(word)
        result=[]
        for k,v in d.items():
            result.append(v)
        return result
