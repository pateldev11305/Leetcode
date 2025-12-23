class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        ans=[]
        if len(nums)==2:
            return [nums[0],nums[1]]
        else:
            for x in nums:
                if x in freq:
                    freq[x] += 1
                else:
                    freq[x] = 1
            for k,v in freq.items():
                if v==1:
                    ans.append(k)
            return ans 