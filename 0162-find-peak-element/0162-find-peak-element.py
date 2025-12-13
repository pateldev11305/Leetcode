import heapq
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=1,len(nums)-2
        n=len(nums)
        if n == 1:
            return 0
        if n == 2:
            if nums[0] > nums[1]:
                return 0 
            else:
                return 1
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        while (l<=h):
            mid=(l+h)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                h=mid-1
            