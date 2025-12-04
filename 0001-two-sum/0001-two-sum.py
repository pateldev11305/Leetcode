class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        #for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
                #if nums[i]+nums[j]==target:
                   # return [i,j]
                #else:
                   # pass
        sol=[]
        for i in range(len(nums)):
            find= target-nums[i]
            if find in nums[i+1:]:
                sol.append(i)
                sol.append(nums.index(find,i+1))
                return sol
            else:
                continue
            