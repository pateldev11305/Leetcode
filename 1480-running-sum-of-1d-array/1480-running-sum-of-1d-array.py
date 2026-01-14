class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        #res=[]
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
            #res.append(sum)
        return nums