class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i in range(len(points)):
            distance=math.sqrt((points[i][0]**2)+(points[i][1]**2))
            dist.append((distance,i))
        heapq.heapify(dist)
        result=[]
        for i in range(k):
            element=heapq.heappop(dist)
            result.append(points[element[1]])
        return result
