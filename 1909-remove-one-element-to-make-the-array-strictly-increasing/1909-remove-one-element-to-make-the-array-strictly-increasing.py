class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count=0
        
        if len(nums)==0 or len(nums)==1:
            return False

        for j in range(len(nums)-1):
            i=0
            if nums[j]>=nums[j+1]:
                count+=1
                i=j+1
                if j > 0 and j + 2 < len(nums) and nums[j - 1] >= nums[i] and nums[j] >= nums[i+1]:

                    return False
        if count>1:
            return False
        else:
            return True
