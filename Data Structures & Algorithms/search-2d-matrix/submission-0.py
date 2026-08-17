class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h=len(matrix)-1
        while l<=h:
            mid=(l+h)//2
            if matrix[mid][-1]<target:
                l=mid+1
            elif matrix[mid][0]>target:
                h=mid-1
            else:
                break
        inner_l=0
        inner_h=len(matrix[mid])-1
        while inner_l<=inner_h:
            new_mid=(inner_l+inner_h)//2
            if matrix[mid][new_mid]<target:
                inner_l=new_mid+1
            elif matrix[mid][new_mid]>target:
                inner_h=new_mid-1
            else:
                return True
        return False    
            