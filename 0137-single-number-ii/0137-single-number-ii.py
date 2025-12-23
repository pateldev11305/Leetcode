class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        if len(nums)==1:
            return nums[0]
        else:
            for x in nums:
                if x in freq:
                    freq[x] += 1
                else:
                    freq[x] = 1
            for k,v in freq.items():
                if v==1:
                    return k 