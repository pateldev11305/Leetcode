class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                 return True
            if nums[mid]==nums[l] and nums[mid]==nums[r] :
                l+=1
                r-=1
            else:
                #left one
                if nums[l]<=nums[mid]:
                    if nums[l]<=target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                #right one
                else :
                    if nums[mid]<=target<=nums[r]:
                        l=mid+1
                    else :
                        r=mid-1
        return False
