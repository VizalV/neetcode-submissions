class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i,val in enumerate(nums):
            if val in count:
                count[val]+=1
            else:
                count[val]=1
        heap=[]
        import heapq
        for key,val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        for tup in heap:
            result.append(tup[1])
        return result
        