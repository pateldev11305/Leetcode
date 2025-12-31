class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        n=len(nums)*2
        ans=[0]*n
        for i in range(len(nums)):
            ans[i],ans[l+i]=nums[i],nums[i]
        return ans