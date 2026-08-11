class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=sorted(nums)
        result=[]
        for i,val in enumerate(arr):
            if i==len(arr)-1:
                return result
            if i>0 and val==arr[i-1]:
                continue         
            l=i+1
            r=len(arr)-1
            while l<r:
                if arr[l]+arr[r]<(0-val):
                    l+=1
                elif arr[l]+arr[r]>(0-val):
                    r-=1
                else:
                    result.append([arr[l],arr[r],val])
                    l+=1
                    while(l<r and arr[l-1]==arr[l]):
                        l+=1