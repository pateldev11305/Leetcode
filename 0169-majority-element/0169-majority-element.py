class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data={}
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        for k,v in data.items():
            if v>len(nums)//2:
                return k
        return 0

