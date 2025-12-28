class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fPtr=0
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[fPtr],nums[i]=nums[i],nums[fPtr]
                    fPtr+=1
        