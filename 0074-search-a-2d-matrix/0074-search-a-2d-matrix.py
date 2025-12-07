class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums=[]
        for i in matrix:
            for j in i:
                nums.append(j)
        nums.sort()
        n=len(nums)-1
        l,r=0,n
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if target>nums[mid]:
                l=mid+1
            if target<nums[mid]:
                r=mid-1
        return False
