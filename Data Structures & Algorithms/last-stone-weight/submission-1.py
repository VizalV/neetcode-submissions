class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            heapq.heapify(stones)
            temp=[]
            l=len(stones)
            for i in range(len(stones)-2):
                temp.append(heapq.heappop(stones))
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            for i in temp:
                heapq.heappush(stones,i)
            if x<y:
                heapq.heappush(stones,y-x)
        if stones:
            return stones[0]
        else:
            return 0
