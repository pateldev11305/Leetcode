class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        u=len(nums)-1
        
        while l<=u:
            mid=(l+u)//2
            if target==nums[mid]:
                return mid

#below is for left sub list
            if nums[l]<=nums[mid]:
                if target<nums[mid] and target>=nums[l]:  #if target lies in left
                    u=mid-1
                    
                else:
                    l=mid+1  #if target lies in right
                    
#below is for right sub list
            else:
                if target>nums[mid] and target<=nums[u]:   #if target lies in right
                    l=mid+1
                    
                else:
                    u=mid-1     #if target lies in left
                    
        return -1


        
        