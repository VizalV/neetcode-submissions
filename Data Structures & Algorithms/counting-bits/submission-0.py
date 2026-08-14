class Solution:
    def countBits(self, n: int) -> List[int]:
        outputs=[]
        for i in range(n+1):
            count=0
            temp=i
            while temp:
                if temp&1:
                    count+=1
                temp>>=1
            outputs.append(count)
        return outputs