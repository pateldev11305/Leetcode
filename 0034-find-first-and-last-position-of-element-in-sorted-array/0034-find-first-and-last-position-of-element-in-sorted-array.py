class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        result=[0,0]
        if not nums:
            return [-1,-1]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                first=mid
                while first>0 and nums[first-1]==target:
                    first-=1

                last=mid
                while last<len(nums)-1 and nums[last+1]==target:
                    last+=1
                return [first,last]
                
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return [-1,-1]
        #return result
